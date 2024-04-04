import requests
from bs4 import BeautifulSoup
import os

ARTICLE_ID = 140211

# 웹 페이지 URL
url = f'https://www.acmicpc.net/board/view/{ARTICLE_ID}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# HTML 요청
response = requests.get(url, headers=headers)

print(response)

# 파일에 쓰기
with open('sample.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

print('HTML 파일이 성공적으로 저장되었습니다.')