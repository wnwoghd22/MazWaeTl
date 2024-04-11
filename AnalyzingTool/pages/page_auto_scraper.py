import requests
from bs4 import BeautifulSoup
import os
import time

'''
https://www.acmicpc.net/ 사이트에 트래픽을 발생시킵니다.
절대 절대 사용하지 마세요.
2024년 4월 5일 기준 백준의 robots.txt는 /board/view 디렉터리에 대한 제한을 걸지 않았습니다.
별도의 meta 태그 또한 포함되어 있지 않습니다.
어쨌든 쓰지 마세요.
'''

for i in range(45,10100):

    ARTICLE_ID = i

    # 웹 페이지 URL
    url = f'https://www.acmicpc.net/board/view/{ARTICLE_ID}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # HTML 요청
    response = requests.get(url, headers=headers)

    # HTML 요청
    response = requests.get(url, headers=headers)

    if response.status_code == 200:  # 응답이 성공적으로 이루어졌을 때만 파일 저장
        print(response)

        # 파일에 쓰기
        with open(f'data/{i}.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

        print('HTML 파일이 성공적으로 저장되었습니다.')

    else:
        print(f'Error: {response.status_code}')

    # 5초간 지연
    time.sleep(5)