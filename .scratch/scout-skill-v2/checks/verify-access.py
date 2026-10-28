"""Bounded read-only connection check; writes summaries, never keys or full bodies.

Run from the repository root with network access. --tavily spends at most two
included credits (one basic search and one single-URL basic extract), only after
verifying a ten-credit buffer. No billing settings or accounts are changed.
This is a ticket verification artifact, not a scout runtime integration.
"""
import argparse
import gzip
import json
import urllib.error
import urllib.request
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--tavily', action='store_true')
parser.add_argument('--output', required=True)
args = parser.parse_args()
results = []


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def request(url, payload=None, headers=None):
    h = {'User-Agent': 'startup-scout-access-check/1.0', **(headers or {})}
    if payload is not None:
        h['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, data=json.dumps(payload).encode() if payload is not None else None, headers=h)
    opener = urllib.request.build_opener(NoRedirect)
    with opener.open(req, timeout=20) as response:
        raw = response.read(2_000_000)
        if raw[:2] == b'\x1f\x8b':
            raw = gzip.decompress(raw)
        data = json.loads(raw)
        limits = {k: response.headers[k] for k in ('X-RateLimit-Limit', 'X-RateLimit-Remaining', 'X-RateLimit-Reset') if k in response.headers}
        return data, limits


def check(name, operation):
    try:
        results.append({'route': name, 'status': 'tested', **operation()})
    except Exception as exc:
        # Do not persist raw exceptions, URLs with credentials, or response bodies.
        results.append({'route': name, 'status': 'failed', 'error_type': type(exc).__name__, 'http_status': getattr(exc, 'code', None)})


def hn():
    base = 'https://hacker-news.firebaseio.com/v0/'
    show, _ = request(base + 'showstories.json')
    ask, _ = request(base + 'askstories.json')
    item, _ = request(base + 'item/30186545.json')
    comment, _ = request(base + 'item/' + str(item['kids'][0]) + '.json')
    assert show and ask and item['type'] == 'story' and comment['type'] == 'comment' and comment.get('text')
    return {'show_count': len(show), 'ask_count': len(ask), 'item_id': item['id'], 'item_fields': sorted(item), 'comment_id': comment['id'], 'comment_fields': sorted(comment), 'comment_text_chars': len(comment['text']), 'coverage': 'two lists, one fixed story, one direct comment; not full traversal'}


def github():
    data, limits = request('https://api.github.com/repos/frappe/erpnext/issues/59726')
    comments, _ = request(data['comments_url'] + '?per_page=1')
    assert data.get('body') and data.get('html_url')
    return {'url': data['html_url'], 'state': data['state'], 'body_chars': len(data['body']), 'comments_returned': len(comments), 'comment_body_chars': len(comments[0].get('body', '')) if comments else 0, 'rate_limits': limits}


def stackexchange():
    base = 'https://api.stackexchange.com/2.3/questions/203604'
    query = '?site=workplace&filter=withbody&pagesize=1'
    data, _ = request(base + query)
    answers, _ = request(base + '/answers' + query) if not data.get('backoff') else ({'items': []}, {})
    item = data['items'][0]
    assert item.get('body')
    return {'url': item['link'], 'body_chars': len(item['body']), 'answers_returned': len(answers['items']), 'answer_body_chars': len(answers['items'][0].get('body', '')) if answers['items'] else 0, 'quota_max': data.get('quota_max'), 'quota_remaining': answers.get('quota_remaining', data.get('quota_remaining')), 'backoff': answers.get('backoff', data.get('backoff')), 'content_license': item.get('content_license'), 'coverage': 'one question and at most one answer; authors and links must accompany reused evidence'}


def tavily():
    key = next(line.split('=', 1)[1].strip().strip('\"\'') for line in Path('.env').read_text().splitlines() if line.startswith('TAVILY_API_KEY='))
    headers = {'Authorization': 'Bearer ' + key}
    def usage():
        data, _ = request('https://api.tavily.com/usage', headers=headers)
        return {k: data['account'].get(k) for k in ('current_plan', 'plan_usage', 'plan_limit', 'paygo_usage', 'paygo_limit')}
    before = usage()
    if not isinstance(before['plan_usage'], (int, float)) or not isinstance(before['plan_limit'], (int, float)) or before['plan_limit'] - before['plan_usage'] < 10:
        return {'status': 'skipped', 'usage_before': before, 'reason': 'Included-credit buffer not verified'}
    search, _ = request('https://api.tavily.com/search', {'query': 'site:ycombinator.com requests for startups', 'search_depth': 'basic', 'max_results': 1, 'include_domains': ['ycombinator.com'], 'include_answer': False, 'include_raw_content': False}, headers)
    extraction, _ = request('https://api.tavily.com/extract', {'urls': ['https://www.ycombinator.com/rfs'], 'extract_depth': 'basic'}, headers)
    assert search.get('results') and search['results'][0].get('content')
    assert extraction.get('results') and extraction['results'][0].get('raw_content')
    return {'usage_before': before, 'search_results': [{'url': x.get('url'), 'content_chars': len(x.get('content', ''))} for x in search.get('results', [])], 'extract_results': [{'url': x.get('url'), 'content_chars': len(x.get('raw_content', ''))} for x in extraction.get('results', [])], 'extract_failed_count': len(extraction.get('failed_results', [])), 'usage_after': usage(), 'transport': 'direct REST; does not establish MCP exposure in this chat'}


check('HN official Firebase API', hn)
check('GitHub public issue and comment REST API', github)
check('Stack Exchange question and answer API', stackexchange)
if args.tavily:
    check('Tavily authenticated REST', tavily)
output = {'checked_date': '2026-10-29', 'date_basis': 'user session date; this artifact is for this ticket', 'results': results}
Path(args.output).write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
