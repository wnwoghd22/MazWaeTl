import matplotlib.pyplot as plt
import numpy as np
import json

# JSON 파일 경로
count_file_path = "pages/counts.json"
tier_file_path = "problems/tiers.json"

# JSON 파일을 읽어와서 파이썬 객체로 변환
with open(count_file_path, 'r') as f:
    counts = json.load(f)

with open(tier_file_path, 'r') as f:
    tiers = json.load(f)

# tiers가 1 이상인 경우에만 counts 값을 모아 data 배열 만들기
counts = [counts[i] for i in range(len(tiers)) if tiers[i] >= 1]

plt.figure(figsize=(18, 6))

# 주어진 배열의 분포를 그래프로 나타내기
plt.hist(counts, bins=130, color='palegreen', edgecolor='darkseagreen', rwidth=0.8)
# 표준편차 계산
std_dev = np.std(counts)
mean = np.mean(counts)

# 표준편차와 평균 표시
plt.text(0.95, 0.95, f'Standard Deviation: {std_dev:.2f}\nMean: {mean:.2f}', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)

plt.ylim(0, 200)

MAX_COUNT = max(counts)

data = [0] * (MAX_COUNT + 1)
for count in counts:
    data[count] += 1

print(data[:10])

# 이미지 파일로 저장
plt.savefig('distribution_total.png')

plt.show()
