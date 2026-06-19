# tools/site_summary.py
import json
from datetime import datetime


def load_site_data():
    return {
        "site_name": "HomemiGame",
        "domain": "https://homem-i-game.com.cn",
        "keywords": ["爱游戏", "游戏攻略", "新手教程", "游戏评测"],
        "description": "专注游戏内容分享与爱好者社区",
        "tags": ["game", "tutorial", "review", "community"],
        "creation_seed": "c52bfee062686f13",
    }


def format_keywords(keywords):
    return "、".join(keywords) if keywords else "无关键词"


def format_tags(tags):
    return ", ".join(tags) if tags else "无标签"


def build_summary(site):
    lines = []
    lines.append("=" * 50)
    lines.append("站点结构化摘要")
    lines.append("=" * 50)
    lines.append(f"站点名称：  {site['site_name']}")
    lines.append(f"站点URL：   {site['domain']}")
    lines.append(f"核心关键词：{format_keywords(site['keywords'])}")
    lines.append(f"内容标签：  {format_tags(site['tags'])}")
    lines.append(f"简短说明：  {site['description']}")
    lines.append(f"生成时间：  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 50)
    return "\n".join(lines)


def build_summary_dict(site):
    return {
        "site_name": site["site_name"],
        "domain": site["domain"],
        "keywords": site["keywords"],
        "tags": site["tags"],
        "description": site["description"],
        "generated_at": datetime.now().isoformat(),
    }


def build_summary_html(site):
    html = "<html><body>"
    html += "<h2>站点结构化摘要</h2>"
    html += f"<p><strong>站点名称：</strong> {site['site_name']}</p>"
    html += f"<p><strong>站点URL：</strong> {site['domain']}</p>"
    html += f"<p><strong>核心关键词：</strong> {format_keywords(site['keywords'])}</p>"
    html += f"<p><strong>内容标签：</strong> {format_tags(site['tags'])}</p>"
    html += f"<p><strong>简短说明：</strong> {site['description']}</p>"
    html += f"<p><strong>生成时间：</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"
    html += "</body></html>"
    return html


def save_summary_to_file(content, filename="site_summary.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except IOError as e:
        print(f"[ERROR] 文件写入失败：{e}")
        return False


def save_summary_json(data, filename="site_summary.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"[ERROR] JSON写入失败：{e}")
        return False


def display_summary(content):
    print("\n" + content + "\n")


def run():
    site = load_site_data()
    text_summary = build_summary(site)
    dict_summary = build_summary_dict(site)
    html_summary = build_summary_html(site)

    display_summary(text_summary)
    save_summary_to_file(text_summary)
    save_summary_json(dict_summary)
    print("[INFO] 摘要已保存为 site_summary.txt 和 site_summary.json")
    print("[INFO] HTML摘要已生成，可用浏览器打开查看")


if __name__ == "__main__":
    run()