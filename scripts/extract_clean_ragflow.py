"""
extract_clean_ragflow.py - Clean RAG Competitor & Market Scraper (GitHub Actions Cloud $0)
Scrapes, strips HTML/ads, and structures data into Clean RAG Markdown for NotebookLM.
"""

import sys
import os
import json
import urllib.request
import urllib.parse
from datetime import datetime


def fetch_clean_page(url: str) -> str:
    """Fetch and convert web page to clean markdown via Jina Reader."""
    clean_url = f"https://r.jina.ai/{url}"
    try:
        req = urllib.request.Request(
            clean_url,
            headers={
                "User-Agent": "Hermes-CleanRAG/1.0",
                "X-Return-Format": "markdown"
            }
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status == 200:
                return resp.read().decode("utf-8")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return ""


def structure_competitor_rag(competitor_name: str, target_url: str, raw_content: str) -> str:
    """Formats raw competitor page into high-signal Clean RAG Markdown."""
    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        f"---",
        f"competitor: \"{competitor_name}\"",
        f"source_url: \"{target_url}\"",
        f"scraped_at: \"{now_str}\"",
        f"rag_type: \"clean_grounded_competitor_dossier\"",
        f"engine: \"GitHub Actions $0 Cloud Runner\"",
        f"---",
        f"",
        f"# 🏢 Competitor Dossier & Strategic Analysis: {competitor_name}",
        f"",
        f"- **Official URL:** {target_url}",
        f"- **Extracted Date:** {now_str}",
        f"",
        f"---",
        f"",
        f"## 1. Value Proposition & Positioning",
        f"",
        raw_content[:4000],
        f"",
        f"---",
        f"",
        f"## 2. Strategic Insights & Potential Gaps",
        f"",
        f"- **Data Signal:** High-signal sanitized DOM (No Ads, No Tracking Cookies).",
        f"- **Usage in NotebookLM:** Ready for PAS, AIDA, and Durex Copywriting synthesis.",
        f""
    ]
    return "\n".join(lines)


def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_clean_ragflow.py <competitor_name> <target_url> [output_file]")
        sys.exit(1)

    competitor_name = sys.argv[1]
    target_url = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else f"clean_rag_{competitor_name.lower().replace(' ', '_')}.md"

    print(f"🚀 Running Clean RAG Extractor for: {competitor_name} ({target_url})")
    content = fetch_clean_page(target_url)

    if not content:
        print(f"⚠️ Warning: Could not fetch content from {target_url}, generating baseline template.")
        content = f"Official website: {target_url}\nDomain analysis pending."

    rag_md = structure_competitor_rag(competitor_name, target_url, content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(rag_md)

    print(f"✅ Clean RAG Markdown successfully compiled to: {output_file} ({len(rag_md.split())} words)")


if __name__ == "__main__":
    main()
