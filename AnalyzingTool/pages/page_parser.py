from bs4 import BeautifulSoup

# sample.html 파일을 읽어서 BeautifulSoup 객체로 파싱
with open('sample.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
    soup = BeautifulSoup(html_content, 'html.parser')

# 모든 태그를 출력
# for tag in soup.find_all():
#   print(tag)

# 클래스가 "content post"인 태그만 찾아서 출력 - 질문자 글
# content_post_tags = soup.find_all(class_="content post")
# for tag in content_post_tags:
#    print(tag)

headers = soup.find_all(class_="page-header")
for tag in headers:
    print(tag)

comments = soup.find_all(class_="col-md-12 comment")
for tag in comments:
    print(tag)