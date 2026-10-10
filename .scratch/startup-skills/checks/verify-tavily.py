"""Bounded setup check; reads a key locally and prints only sanitized results."""
import json
from pathlib import Path
import urllib.error
import urllib.request


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def main():
    key = ""
    for line in (Path(__file__).resolve().parents[3] / ".env").read_text().splitlines():
        if line.startswith("TAVILY_API_KEY="):
            key = line.split("=", 1)[1].strip().strip("\"'")
    if not key:
        raise RuntimeError("Missing key")
    opener = urllib.request.build_opener(NoRedirect)
    headers = {
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }

    def emit(data):
        print(json.dumps(data).replace(key, "[REDACTED]"), flush=True)

    def usage():
        request = urllib.request.Request(
            "https://api.tavily.com/usage",
            headers={"Authorization": "Bearer " + key, "Accept": "application/json"},
        )
        with opener.open(request, timeout=30) as response:
            account = json.load(response)["account"]
        return {field: account.get(field) for field in (
            "current_plan", "plan_usage", "plan_limit", "paygo_usage", "paygo_limit"
        )}

    def rpc(payload):
        request = urllib.request.Request(
            "https://mcp.tavily.com/mcp/", headers=headers,
            data=json.dumps(payload).encode(),
        )
        with opener.open(request, timeout=45) as response:
            if response.headers.get("Mcp-Session-Id"):
                headers["Mcp-Session-Id"] = response.headers["Mcp-Session-Id"]
            raw = response.read().decode()
            if not raw.strip():
                return {}
            if response.headers.get("Content-Type", "").startswith("text/event-stream"):
                for line in raw.splitlines():
                    if line.startswith("data:"):
                        item = json.loads(line[5:].strip())
                        if item.get("id") == payload.get("id"):
                            return item
                raise RuntimeError("No matching MCP response")
            return json.loads(raw)

    before = usage()
    emit({"usage_before": before})
    if not isinstance(before["plan_limit"], (int, float)) or not isinstance(before["plan_usage"], (int, float)):
        raise RuntimeError("Cannot establish included allowance")
    if before["plan_limit"] - before["plan_usage"] < 10:
        raise RuntimeError("Insufficient included allowance for bounded check")
    initialization = rpc({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
        "protocolVersion": "2025-03-26", "capabilities": {},
        "clientInfo": {"name": "startup-scout-setup-check", "version": "1.0"},
    }})
    headers["MCP-Protocol-Version"] = initialization["result"]["protocolVersion"]
    rpc({"jsonrpc": "2.0", "method": "notifications/initialized"})
    listed = rpc({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
    exposed = {tool["name"] for tool in listed["result"]["tools"]}
    target = "https://www.ycombinator.com/rfs"
    bounded_site = {"url": target, "max_depth": 1, "max_breadth": 1, "limit": 1, "allow_external": False}
    checks = [
        ("tavily_search", {"query": "Y Combinator Requests for Startups", "include_domains": ["ycombinator.com"], "max_results": 1, "search_depth": "basic"}),
        ("tavily_extract", {"urls": [target], "extract_depth": "basic", "format": "text"}),
        ("tavily_map", bounded_site),
        ("tavily_crawl", {**bounded_site, "extract_depth": "basic", "format": "text"}),
    ]
    for identifier, (name, arguments) in enumerate(checks, 3):
        if name not in exposed:
            emit({"tool": name, "status": "not_exposed"})
            continue
        reply = rpc({"jsonrpc": "2.0", "id": identifier, "method": "tools/call", "params": {"name": name, "arguments": arguments}})
        result = reply.get("result", {})
        texts = [block.get("text", "") for block in result.get("content", []) if block.get("type") == "text"]
        joined = "\n".join(texts)
        summary = {"tool": name, "rpc_error": bool(reply.get("error")), "tool_error": bool(result.get("isError")), "text_characters": len(joined), "excerpt": joined[:400]}
        for entry in texts:
            try:
                parsed = json.loads(entry)
                if isinstance(parsed, dict):
                    summary["result_count"] = len(parsed.get("results", []))
                    summary["failed_result_count"] = len(parsed.get("failed_results", []))
            except (ValueError, TypeError):
                pass
        emit(summary)
    after = usage()
    emit({"usage_after": after, "plan_credit_delta": after["plan_usage"] - before["plan_usage"]})


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as error:
        print(json.dumps({"status": "failed", "http_status": error.code}), flush=True)
        raise SystemExit(1)
    except Exception as error:
        print(json.dumps({"status": "failed", "error_type": type(error).__name__}), flush=True)
        raise SystemExit(1)
