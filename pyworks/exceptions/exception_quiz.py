# 실습문제1 - 정수 입력하기1
while True:
    try:
        num = int(input("숫자 입력: "))
    except ValueError as e:
        print('정수가 아닙니다. 정수를 입력해주세요!')
    else:
        print(f'정수 입력 성공: {num}')
        break

# 실습문제1 - 정수 입력하기2
    while True:
        try:
            num = int(input("숫자 입력: "))
            break
        except ValueError:
            print('정수가 아닙니다. 정수를 입력해주세요!')

print(f'정수 입력 성공: {num}')