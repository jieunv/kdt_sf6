'''
유용한 문자열 함수
전체 개수 - len() , 특정한 문자 개수 - 문자열.count()
대문자 변환 - 문자열. upper(), 소문자 - 문자열.lower()
문자열을 잘라서 리스트로 반환 - 문자열.split(구분기호)
특정한 문자를 변경 - replace(old, new)
'''

f = "바나나"
print(len(f))
print(len("banana"))


print("banana".count("a"))  # "banana"에서 a의 개수를 출력한다

upper_case = "Hello".upper()
lower_case = "Hello".lower()
print(upper_case, lower_case)

friends = "존 루나 제리"
print(friends.split(" ")) # 구분기호 - 공백문자

alpa = "a:b:c:d"
print(alpa.split(":"))  # :은 구분 기호

email = "codingOn@spreatics.com"
print(email.split("@"))

# replace()
msg = "Hello Python"
print(msg.replace(__old="Python", __new="C++"))






