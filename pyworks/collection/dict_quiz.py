# 1. 빈 딕셔너리 생성
dict1 = {}

# 2.데이터 추가
dict1 = {
    "Alice": "85",
    "Bob": "90",
    "Charlie": "95"
}
print(dict1)

# 3. 학생 추가
dict1["David"] = "80"
print(dict1)

# 4. 학생 점수 수정
dict1["Alice"] = "88"
print(dict1)

# 5. 학생 삭제
dict1.pop('Bob')
print(dict1)

# 6. 학생 전체 출력
for key in dict1:
    print(f'{key}:{dict1[key]}')