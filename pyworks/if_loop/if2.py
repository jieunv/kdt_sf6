# 다중 조건문
"""
if 조건1:
    실행문(조건1 참일 대)
elif 조건2:
    실행문(조건2 참일때)
else:
    실행문(조건1과 2가 모두 거짓일 때)
"""

age = 25
if 0 >= age < 20: #0 < age < 0
    print("미성년자 입니다.")
elif age >= 20 and age < 30:
    print("30대 입니다.")
elif age >= 30 and age < 40:
    print("40대 입니다.")
else:
    print("이제는 중년...")
print(f'나이는 {age}세 입니다.')

