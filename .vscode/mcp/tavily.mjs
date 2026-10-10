import { fileURLToPath } from 'node:url';

if (!process.env.TAVILY_API_KEY?.trim()) {
  console.error('Missing TAVILY_API_KEY. Add it to the workspace .env and restart Tavily.');
  process.exit(1);
}

// VS Code loads envFile for stdio servers. Let the bridge expand the header
// inside this process so the key is absent from config, URLs and process args.
delete process.env.HUNTER_API_KEY;
delete process.env.APOLLO_API_KEY;
const proxy = new URL('./node_modules/mcp-remote/dist/proxy.js', import.meta.url);
process.argv = [
  process.execPath,
  fileURLToPath(proxy),
  'https://mcp.tavily.com/mcp/',
  '--header', 'Authorization: Bearer ${TAVILY_API_KEY}',
  '--transport', 'http-only',
  '--silent',
  '--ignore-tool', 'tavily_research',
];
await import(proxy.href);
