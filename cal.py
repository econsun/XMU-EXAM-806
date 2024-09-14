import os
import re

file_path = r"C:\Users\29848\OneDrive\Obsidian\806-XMU\Preface.md"

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: 清空 <p style="font-size:x-large;"> 标签中的内容
content = re.sub(r'<p style="font-size:x-large;">[^<]*</p>', 
                 '<p style="font-size:x-large;"></p>', content)

# 提取链接
pattern = r'\[\[(.*?)\|.*?\]\]'
matches = re.findall(pattern, content)
total_links = len(matches)

directory_path = r"C:\Users\29848\OneDrive\Obsidian\806-XMU"
found_files = 0

def file_exists_in_numeric_directories(filename, root_directory):
    for root, dirs, files in os.walk(root_directory):
        current_folder = os.path.basename(root)
        if current_folder.isdigit():
            if f"{filename}.md" in files:
                return True
    return False

for filename in matches:
    if file_exists_in_numeric_directories(filename, directory_path):
        found_files += 1

found_ratio = found_files / total_links if total_links > 0 else 0
found_ratio_percent = round(found_ratio * 100, 2)

# Step 2: 插入新的进度百分比
# 找到包含"进度："的 <p> 标签并更新其内容
new_content = re.sub(
    r'<p style="font-size:x-large;">.*?</p>',
    f'<p style="font-size:x-large;">厦门大学 806 宏、微观经济学历年真题解析完成进度：{found_ratio_percent}%</p>',
    content
)

# 将修改后的内容写回文件
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)