# 다중 예외 처리
'''
try:
    num = [1,2,3,4]


# 3가지의 에러 - 다중 에러 처리
    num[10]    # IndexError
    num[3] / 0 # ZeroDivisionError
    # print(who)   # NameError
    
except IndexError:
    print("인덱스 에러 발생")
except ZeroDivisionError:
    print("0으로 나눌 수 없음")
except ZeroDivisionError:
    print("존재하지 않는 변수 호출")
else:
    print("예외 없음!! ")
'''

# 입력 받을 때 에러 처리
try:
    num = int(input("숫자 입력: "))
except ValueError as e:
    # print('정수가 아닙니다. 정수를 입력해주세요')
    print(e) # print(exception)




