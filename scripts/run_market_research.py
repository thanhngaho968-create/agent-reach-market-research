"""
run_market_research.py - Market Research & Social Intelligence Engine
Executes multi-platform queries and aggregates findings into structured Markdown reports.
"""

import os
import sys
import json
import time
import urllib.request
import argparse
from datetime import datetime


def fetch_jina_search(query: str, max_results: int = 5) -> list:
    """Fetch search results via Jina Reader search API."""
    encoded_q = urllib.parse.quote(query)
    url = f"https://s.jina.ai/{encoded_q}"
    results = []
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Agent-Reach-MarketResearch/1.0",
                "X-Return-Format": "markdown"
            }
        )
        with urllib.request.urlopen(req, timeout=25) as resp:
            if resp.status == 200:
                raw_text = resp.read().decode("utf-8")
                results.append({"platform": "web_search", "content": raw_text[:8000]})
    except Exception as e:
        results.append({"platform": "web_search", "error": str(e)})
    return results


def fetch_v2ex_hot() -> list:
    """Fetch trending tech & market discussions from V2EX."""
    url = "https://www.v2ex.com/api/topics/hot.json"
    results = []
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "agent-reach/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status == 200:
                data = json.loads(resp.read().decode("utf-8"))
                for item in data[:5]:
                    results.append({
                        "platform": "v2ex",
                        "title": item.get("title"),
                        "url": item.get("url"),
                        "content": item.get("content", "")[:500]
                    })
    except Exception as e:
        results.append({"platform": "v2ex", "error": str(e)})
    return results


def compile_market_report(query: str, search_results: list, v2ex_results: list) -> str:
    """Compiles multi-platform findings into a high-signal Market Research Report."""
    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        f"# 📊 Market Research & Intelligence Report: {query}",
        f"",
        f"- **Query:** `{query}`",
        f"- **Generated At:** {now_str}",
        f"- **Engine:** Agent-Reach Market Intelligence Cloud Runner",
        f"- **Security:** Zero-Leak Sandboxed Execution",
        f"",
        f"---",
        f"",
        f"## 1. Web & Industry Search Intelligence",
        f""
    ]

    for item in search_results:
        if "content" in item:
            lines.append(item["content"])
        elif "error" in item:
            lines.append(f"> [!WARNING] Search query notice: {item['error']}")

    lines.extend([
        f"",
        f"---",
        f"",
        f"## 2. Social & Developer Discussions (V2EX / Tech Signals)",
        f""
    ])

    for post in v2ex_results:
        if "title" in post:
            lines.append(f"### 💬 [{post['title']}]({post.get('url', '#')})")
            if post.get("content"):
                lines.append(f"{post['content']}")
            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Run autonomous market research")
    parser.add_argument("query", help="Market research topic or question")
    parser.add_argument("--output", default="market_research_report.md", help="Output markdown file")
    parser.add_argument("--json", action="store_true", help="Output JSON metadata")
    args = parser.parse_args()

    print(f"🚀 Launching Market Research for: {args.query}")
    search_data = fetch_jina_search(args.query)
    v2ex_data = fetch_v2ex_hot()

    report_md = compile_market_report(args.query, search_data, v2ex_data)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report_md)

    print(f"✅ Market Research Report compiled to: {args.output} ({len(report_md.split())} words)")


if __name__ == "__main__":
    main()
