import os
from bs4 import BeautifulSoup
import json

# data 폴더 내의 모든 파일 목록 가져오기
file_list = os.listdir('data')

# JSON 파일로 저장할 디렉토리 생성
if not os.path.exists('output'):
    os.makedirs('output')

# 각 파일에 대해 처리
for idx in range(141740):
    if idx % 1000 == 0:
        print(f"processing {idx}...")

    # 해당 ID에 대한 HTML 파일이 있는 경우에만 처리
    if os.path.isfile(os.path.join('data', f'{idx}.html')):
        # print(f'parsing {idx}.html')
        
        # 해당 ID에 대한 JSON 파일 경로 설정
        json_file_path = os.path.join('output', f'{idx}.json')
    
        # HTML 파일 읽어오기
        with open(os.path.join('data', f'{idx}.html'), 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        # 질문 제목 추출
        questionTitle = soup.select_one('.page-header h3').get_text().strip()

        # 문제 번호 추출
        problem_tag = soup.select_one('.page-header blockquote a')

        if problem_tag:
            problemNumber = soup.select_one('.page-header blockquote a')['href'].split('/').pop()
        else:
            problemNumber = -1

        # JSON 배열을 저장할 변수 생성
        comments = []

        # 모든 댓글 선택
        commentElements = soup.select('.col-md-12.comment')

        # 각 댓글을 순회하며 정보 추출
        for commentElement in commentElements:
            # 작성자 추출
            author = commentElement.select_one('.panel-title a').get_text().strip()

            # 작성 일자(timestamp) 추출
            timestamp = int(commentElement.select_one('.real-time-update')['data-timestamp'])

            # 내용 추출
            content = commentElement.select_one('.content').get_text().strip()

            # textarea가 있는 경우
            textarea = commentElement.find('textarea')
            if textarea:
                # 언어 종류 추출
                language = textarea['data-mime']
                # 코드 추출
                code = textarea.get_text().strip()
                # JSON 객체에 코드 정보 추가
                codeObject = {
                    "language": language,
                    "code": code
                }
                # JSON 배열에 추가
                comments.append({
                    "author": author,
                    "timestamp": timestamp,
                    "content": content,
                    "code": codeObject
                })
            else:
                # textarea가 없는 경우
                # JSON 객체에 저장
                comments.append({
                    "author": author,
                    "timestamp": timestamp,
                    "content": content
                })

        # 최종 JSON 객체 생성
        finalObject = {
            "title": questionTitle,
            "problem_id": problemNumber,
            "comments": comments
        }

        # JSON 파일로 저장
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(finalObject, json_file, ensure_ascii=False, indent=2)
