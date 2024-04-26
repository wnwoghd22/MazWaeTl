import os
import json

file_list = os.listdir('output')

# JSON 파일로 저장할 디렉토리 생성
if not os.path.exists('problems'):
    os.makedirs('problems')

# 각 문제를 problem_id로 분류하여 저장할 딕셔너리 생성
problems = {}

cnts = [0] * 150_000

progress = 0

for file_name in file_list:
    progress += 1
    if progress % 1000 == 0:
        print(f"progressing...{progress}")

    json_file_path = os.path.join("output", file_name)

    # JSON 파일 불러오기
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 각 문제의 problem_id를 기준으로 파일 분류
    problem_id = int(data["problem_id"])
    if problem_id not in problems:
        problems[problem_id] = []
    problems[problem_id].append(json_file_path)

    if problem_id == -1:
        cnts[0] += 1 # etc
    else: 
        cnts[problem_id] += 1

        folder_name = f"problems/{problem_id}"
        os.makedirs(folder_name, exist_ok=True)  # 폴더가 없으면 생성, 이미 있으면 pass

        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

counts_file_path = "counts.json"
with open(counts_file_path, 'w') as f:
    json.dump(cnts, f)