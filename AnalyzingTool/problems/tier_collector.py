import requests
from bs4 import BeautifulSoup
import json
import time

PROBLEMS_COUNT = 40000

ls = [0] * PROBLEMS_COUNT

for lv in range(30):
    with open(f'tier-{lv + 1}.json', 'r') as f:
        json_content = f.read()
        problems = json.loads(json_content)

        for idx in problems:
            ls[idx] = lv + 1

# 파일에 쓰기
with open('tiers.json', 'w', encoding='utf-8') as f:
    txt = json.dumps(ls)
    f.write(txt)
