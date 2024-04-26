import matplotlib.pyplot as plt
import json

LIMIT = 1000

# JSON 파일 경로
count_file_path = "pages/sorted_counts.json"
tier_file_path = "problems/tiers.json"

# JSON 파일을 읽어와서 파이썬 객체로 변환
with open(count_file_path, 'r') as f:
    data = json.load(f)

with open(tier_file_path, 'r') as f:
    tiers = json.load(f)

# 상위 30개 표시
data = data[1:LIMIT+1]

# 배열에 있는 index 추출
indexes = [str(x[0]) for x in data]
difficulty_colors = [
    'black', # 0
    'saddlebrown', 'saddlebrown', 'saddlebrown', 'sienna', 'sienna',
    'dimgray', 'dimgray', 'gray', 'gray', 'silver',
    'gold', 'gold', 'gold', 'yellow', 'yellow',
    'springgreen', 'springgreen', 'springgreen', 'mediumspringgreen', 'mediumspringgreen',
    'darkturquoise','darkturquoise', 'cyan', 'cyan', 'cyan',
    'mediumvioletred', 'mediumvioletred', 'deeppink', 'deeppink', 'hotpink' 
]

# 배열에 있는 count 추출
counts = [x[1] for x in data]

# 난이도 추출
difficulties = [tiers[x[0]] for x in data]
colors = [difficulty_colors[difficulty] for difficulty in difficulties]

plt.figure(figsize=(12, 6))

# 히스토그램 그리기
plt.bar(indexes, counts, color=colors)

plt.xticks(rotation=-45)  # x축 라벨 회전

# 이미지 파일로 저장
plt.savefig(f'histogram_top{LIMIT}.png')

plt.show()
