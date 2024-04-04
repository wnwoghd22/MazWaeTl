import requests
from bs4 import BeautifulSoup
import json
import time

PAGE_SIZE = 50
CLASS = 'css-q9j30p'

api_url = 'https://solved.ac/api/v3/problem/level'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(api_url + '?query=""', headers=headers)
levels = json.loads(response.text)

for level_dict in levels:
    level = level_dict['level']
    count = level_dict['count']

    if level == 0: continue

    url = f'https://solved.ac/problems/level/{level}?page='
    pages = count // PAGE_SIZE + (1 if count % PAGE_SIZE != 0 else 0)

    ls = []

    for i in range(pages):
        response = requests.get(url + str(i + 1), headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        tags = soup.find_all(class_=CLASS)
        for tag in tags:
            ls.append(tag.text)

        time.sleep(1)

    json_data = json.dumps(list(map(int, ls[::2])))

    with open(f'tier-{level}.json', 'w') as json_file:
        json_file.write(json_data)

    print(f'tier-{level}.json saved.')