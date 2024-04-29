'''
어떤 문장에 더 많은 정보가 있는가?
질문보다는 대답에 유효한 정보가 더 많을 것이라 판단.
comments의 길이가 2 이상인 경우, 두 번째부터 끝까지의 문장들을 모두 모은 후
토큰을 분석하여 많은 순서대로 정렬하고자 함.

본 스크립트는 문장을 모으는 작업을 함.
'''
import os
import json

sentences = []

# data 폴더 내의 모든 파일 목록 가져오기
file_list = os.listdir('output')

cnt = 0

for file_name in file_list:
    cnt += 1
    if cnt % 1000 == 0:
        print(f"processing {cnt}...")
    # print(file_name)
    
    # HTML 파일 읽어오기
    with open(os.path.join('output', file_name), 'r', encoding='utf-8') as file:
        data = json.load(file)

    # print(data)
    if data.get('comments') and len(data['comments']) > 1:
        for e in data['comments'][1:]:
            sentences.append(e['content'])

# print(sentences)

# JSON 파일로 저장
with open('answer_sentences.json', 'w', encoding='utf-8') as json_file:
    json.dump(sentences, json_file, ensure_ascii=False, indent=2)
print("done")