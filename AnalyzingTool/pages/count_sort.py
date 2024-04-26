import json

# JSON 파일 경로
json_file_path = "counts.json"

# JSON 파일을 읽어와서 파이썬 객체로 변환
with open(json_file_path, 'r') as f:
    count_arr = json.load(f)

length = len(count_arr)
print(length)

counts = [(i, count_arr[i]) for i in range(length)]
sorted_counts = sorted(counts, key=lambda x: -x[1])

with open("sorted_counts.json", 'w') as f:
    json.dump(sorted_counts, f)