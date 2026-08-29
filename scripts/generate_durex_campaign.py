"""
generate_durex_campaign.py - Full-Stack Durex Copywriting & Campaign Generator (GitHub Actions Cloud $0)
Applies the 8 Durex Formulas to generate Titles, Social Posts, Hooks, Video Scripts, and Poster metadata.
"""

import sys
import os
import json
from datetime import datetime


def generate_durex_campaign(topic: str, product_usp: str, target_audience: str, competitor: str = "") -> dict:
    """Generates full multi-format Durex-style marketing suite."""
    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    campaign = {
        "topic": topic,
        "product_usp": product_usp,
        "target_audience": target_audience,
        "competitor": competitor,
        "created_at": now_str,
        "formulas_used": [
            "1. 谐音置换 (Homophone Metaphor)",
            "2. 数字双关 (Numerical Double Meaning)",
            "3. 词义劫持 (Industry Jargon Hijack)",
            "4. 场景移植 (Object Monologue)",
            "5. 拆字重组 (Visual Wordplay)",
            "6. 对仗宜忌体 (Antithetical Contrast & Do/Don't)",
            "7. 诗歌白描 (Minimalist Free Verse)",
            "8. 反向克制 (Profound Understatement)"
        ],
        "viral_hooks": [
            f"Người thông minh hoàn thành trong 5 phút. Kẻ khác vẫn đang loay hoay với {competitor or 'công cụ cũ'}.",
            f"199 ngày sau bạn sẽ không nhớ số tiền này, nhưng sẽ nhớ sự vượt trội này.",
            f"Không phải AI có ảo giác, là bạn chưa biết cách làm chủ nó.",
            f"Cái máy in nói: 'Đã 3 tháng rồi không ai bắt tôi in lại bản sửa đổi nào nữa'.",
            f"Học công cụ thì tốn công. Học tư duy thì thông trăm đường.",
            f"Dùng 3 giờ hôm nay, đổi lấy 3 năm không phải tăng ca vô nghĩa."
        ],
        "short_video_scripts": [
            {
                "title": f"Bóc Mẽ Điểm Yếu Của {competitor or 'Thị Trường'}",
                "duration": "45s",
                "structure": {
                    "0-5s_Hook": f"90% người làm {topic} đang tốn gấp 10 lần thời gian vì một sai lầm chết người.",
                    "6-25s_Story": f"Minh họa tình huống khách hàng bị kẹt với giải pháp cũ, tốn hàng giờ mà không ra kết quả.",
                    "26-40s_Breakdown": f"Điểm đột phá: {product_usp}. Một bước nhảy thay đổi toàn bộ cuộc chơi.",
                    "41-45s_CTA": "Theo dõi kênh để nhận trọn bộ cẩm nang tối ưu quy trình ngay hôm nay."
                }
            }
        ],
        "social_posts": [
            {
                "platform": "Facebook / LinkedIn / XiaoHongShu",
                "eyebrow": "CHIẾN LƯỢC · ĐỘT PHÁ NĂNG SUẤT",
                "headline": "Người hiểu luật chơi, không cần phải chạy đua.",
                "body": f"Trong khi mọi người mải miết chạy theo từng trào lưu, người chiến thắng chỉ tập trung vào một điểm tựa duy nhất: {product_usp}.\n\nĐánh trúng một điểm, gãy cả một thành trì. Đừng để năng suất của bạn bị giới hạn bởi tư duy cũ."
            }
        ],
        "poster_params": {
            "eyebrow": "HERMES · STRATEGIC MARKETING",
            "headline": "Người hiểu luật chơi, không cần phải chạy đua.",
            "highlight": "hiểu luật chơi",
            "subtext": "Đánh trúng một điểm, gãy cả một thành trì.",
            "theme": "brand_red",
            "ratio": "3x4"
        }
    }
    return campaign


def format_campaign_markdown(campaign: dict) -> str:
    """Renders campaign into clean, structured Markdown."""
    lines = [
        f"# 🎭 Trọn Bộ Chiến Dịch Marketing Phong Cách Durex Copywriting",
        f"",
        f"- **Chủ đề:** `{campaign['topic']}`",
        f"- **Định vị & USP:** `{campaign['product_usp']}`",
        f"- **Đối tượng:** `{campaign['target_audience']}`",
        f"- **Thời gian tạo:** {campaign['created_at']}",
        f"- **Engine:** Durex Copywriter Full-Suite Cloud Runner ($0 Compute)",
        f"",
        f"---",
        f"",
        f"## 1. Danh Sách 6 Viral Hooks (Áp Dụng 8 Công Thức Vàng)",
        f""
    ]
    for i, h in enumerate(campaign["viral_hooks"], 1):
        lines.append(f"{i}. **{h}**")

    lines.extend([
        f"",
        f"---",
        f"",
        f"## 2. Kịch Bản Video Ngắn TikTok / Shorts (45 Giây)",
        f""
    ])
    for s in campaign["short_video_scripts"]:
        lines.append(f"### 🎬 {s['title']} ({s['duration']})")
        for stage, text in s["structure"].items():
            lines.append(f"- **[{stage}]:** {text}")
        lines.append("")

    lines.extend([
        f"---",
        f"",
        f"## 3. Bài Viết Mạng Xã Hội (Facebook / XiaoHongShu / LinkedIn)",
        f""
    ])
    for p in campaign["social_posts"]:
        lines.append(f"### 📌 `{p['eyebrow']}` — **{p['headline']}**")
        lines.append(f"{p['body']}")
        lines.append("")

    return "\n".join(lines)


def main():
    topic = sys.argv[1] if len(sys.argv) > 1 else "Tự Động Hóa Quy Trình R&D"
    usp = sys.argv[2] if len(sys.argv) > 2 else "Hệ Thống Dual-Node Tự Động Toàn Diện"
    audience = sys.argv[3] if len(sys.argv) > 3 else "Solopreneurs & Tech Leaders"
    comp = sys.argv[4] if len(sys.argv) > 4 else "Công cụ thủ công"
    output_md = sys.argv[5] if len(sys.argv) > 5 else "durex_campaign_suite.md"

    campaign = generate_durex_campaign(topic, usp, audience, comp)
    md_content = format_campaign_markdown(campaign)

    with open(output_md, "w", encoding="utf-8") as f:
        f.write(md_content)

    with open("durex_poster_params.json", "w", encoding="utf-8") as f:
        json.dump(campaign["poster_params"], f, indent=2, ensure_ascii=False)

    print(f"✅ Durex Full-Suite Campaign compiled to: {output_md}")


if __name__ == "__main__":
    main()
