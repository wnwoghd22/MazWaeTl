import matplotlib.pyplot as plt
import json

# JSON 파일 경로
count_file_path = "pages/sorted_counts.json"
tier_file_path = "problems/tiers.json"

# JSON 파일을 읽어와서 파이썬 객체로 변환
with open(count_file_path, 'r') as f:
    data = json.load(f)

with open(tier_file_path, 'r') as f:
    tiers = json.load(f)

# 배열에 있는 index 추출
indexes = [
    'Etc',
    'B5', 'B4', 'B3', 'B2', 'B1',
    'S5', 'S4', 'S3', 'S2', 'S1',
    'G5', 'G4', 'G3', 'G2', 'G1',
    'P5', 'P4', 'P3', 'P2', 'P1',
    'D5', 'D4', 'D3', 'D2', 'D1',
    'R5', 'R4', 'R3', 'R2', 'R1'
]

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
counts = [0] * 31
for x in data:
    counts[tiers[x[0]]] += x[1]

plt.figure(figsize=(12, 6))

# 히스토그램 그리기
plt.bar(indexes, counts, color=difficulty_colors)

plt.xticks(rotation=-45)  # x축 라벨 회전

# 이미지 파일로 저장
plt.savefig(f'histogram_by_tier.png')

plt.show()
