import os
from bs4 import BeautifulSoup

def inject_ads_script(soup):
    if soup.body is None:
        print("⚠️ 无法注入广告：该文件缺少 <body> 标签。")
        return False
    ads_script = soup.new_tag("script", src="ads.js")
    soup.body.append(ads_script)
    return True

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    if inject_ads_script(soup):
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f"✅ 已插入广告：{filepath}")
    else:
        print(f"⛔ 跳过文件：{filepath}")

def process_site():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html") and not file.startswith("google"):
                filepath = os.path.join(root, file)
                process_html_file(filepath)

if __name__ == "__main__":
    process_site()
    input("操作完成，按任意键退出...")
