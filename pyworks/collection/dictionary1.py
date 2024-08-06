# 자료구조 - dictionary (데이터 관리의 4가지: 생성, 조회, 수정, 삭제)
# "치킨" : "닭을 튀긴 요리", key(키): value(값) - 낱말이 있으면 정의가 있듯이 키와 값이 한 쌍이 된다.
# {} 중괄호 사용

# 빈 딕셔너리 생성1
dict2 = {}
print(dict2)
# 빈 딕셔너리 생성2
dict2 = dict()
print(dict2)


# ftuits = ['apple', 'banana', 'cherry']
fruits = {
    "apple": "사과",
    "banana": "바나나",
    "peach": "복숭아"
}

# 접근, 검색, 조회
print(fruits["apple"])
# print(fruits["tomato"]) keyError - "tomato"라는 키는 없기에 키에러가 뜬다

# get()을 이용한 검색
print(fruits.get(""))
print(fruits.get("tonato")) #ERROR가 아닌 none이 출력된다

# 요소 추가/생성
fruits["strawberry"] = "딸기"
print(fruits)
print(type(fruits)) #<class 'dict'>라고 출력됨

# 요소 수정/변경/업데이트 - 추가와 다른 점은 리스트에 키가 있냐 없냐
fruits["peach"] = "천도복숭아"
print(fruits)

# 요소 삭제 - pop() 함수 사용
fruits.pop("banana")
print(fruits)

# 키만 반환
print(fruits.keys())

# 값만 반환
print(fruits.values())

# 키와 값 전체 반환
print(fruits.items()) #key와 value 값이 모두 리스트 형태로 출력된다.

# 키와 값 전체 조회
for key in fruits:
    print(key, ':' , fruits[key]) #fruits[key]가 value값이 된다.

# 딕셔너리 생성
dict1 = {1:'a', 2:'b', 3:'c'}
print(dict1)

# key = 4, value = 'd'를 추가하기
dict1["4"] = "d"
print(dict1)

# for문을 이용한 전체 조회
for key in dict1:
    # print(key, ':', dict1[key])
    print(f'{key} : {dict1[key]}')

# 요소 수정 - key 3의 값을 k로 변경
dict1[3] = "k"
print(dict1)

# 요소 삭제 - key 2번 삭제
dict1.pop(2)
print(dict1)

