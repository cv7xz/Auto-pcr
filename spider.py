import requests
import re

url = "https://wiki.biligame.com/pcr/%E8%A7%92%E8%89%B2%E5%9B%BE%E9%89%B4"

req = requests.get(url=url)

with open('text.txt','w',encoding='utf-8') as f:
    f.write(req.text)


list = re.findall(r'alt="(.*?)" src.*? width="60" height="60"', req.text)

seen = set()
result = []
for item in list:
    if item not in seen:
        seen.add(item)
        result.append(item)

print(result)  # [1, 2, 3, 4]

url_prefix = 'https://wiki.biligame.com/pcr/'


import time,csv
with open("ocr_result3.csv", mode="w", encoding="utf-8-sig", newline="") as file:
    for name in result:
        url = url_prefix + name
        req = requests.get(url=url)
        insert_text = re.search(r'碎片获取(.*?)</td></tr>', req.text, re.DOTALL)
        segment = insert_text.group(1)
        # 提取这一段中所有 title
        titles = re.findall(r'title="(.*?)"', segment)
        print(titles)

        print(name,titles)

        writer = csv.writer(file)
        writer.writerow([name,titles])  # 写入单列
        time.sleep(0.1)
