# 🌐 Agent-Reach: Autonomous Market Research & Intelligence Engine

A cloud-native, zero-leak Autonomous Market Research and Social Intelligence Router designed to operate seamlessly on GitHub Actions ($0 Cloud Compute) and integrate with Google NotebookLM & Hermes Agent.

---

## ⚡ Core Capabilities
- **Multi-Platform Intelligence:** Scans across 15+ information channels (Exa Search, Jina Reader, Reddit, Twitter/X, Bilibili, XiaoHongShu, V2EX, RSS).
- **$0 Cloud Runner Architecture:** Offloads intensive web scraping, transcript extraction, and market synthesis to GitHub Actions runners.
- **Strict Zero-Leak Security:** Enforces strict Gitleaks audits, zero hardcoded credentials, secret masking, and clean sandboxing.
- **NotebookLM Synergy:** Formats synthesized market intelligence into clean Markdown with YAML Frontmatter for instant deep R&D analysis in Google NotebookLM.

---

## 🛡️ Anti-Leak & Security Architecture
1. **GitHub Secrets Only:** All tokens, cookies, and keys must be injected exclusively via GitHub Secrets.
2. **Pre-commit Gitleaks:** Automated CI workflow runs Gitleaks on all commits and pull requests.
3. **Zero Local Persistence:** Output artifacts are pushed directly to cloud storage and deleted from runners upon job completion.

---

## 🚀 Triggering Market Research via API
```bash
# Repository Dispatch Event
curl -X POST https://api.github.com/repos/thanhngaho968-create/agent-reach-market-research/dispatches \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -d '{
    "event_type": "market_research_event",
    "client_payload": {
      "query": "Competitor Analysis: Autonomous AI Agent Frameworks 2026",
      "notebook_id": "0383ceb1-10c1-46ac-9111-d7c728cc0f32"
    }
  }'
```

---

## 📜 License
MIT License. Open-source and safe for autonomous agent orchestration.
