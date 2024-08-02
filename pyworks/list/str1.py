# 문자열은 특별한 1차원 리스트

msg = "Have a nice day!"
print(msg[0])
print(msg[-1])
print(msg[0:4])

#nice day!
print(msg[7:])  # 문자열에서 띄어쓰기도 하나의 문자로 생각해야 한다.

# 문자열 포맷 서식
# %d -정수, %s - 문자열, %f - 실수
print("나는 이번 달에 책을 %d권 샀어요" % 2 )   # d는 정수에 상응
print("나는 이번 달에 책을 %s권 샀어요" % '두' )  # s는 문자에 상응

count = 2
print("나는 이번 달에 책을 %d권 샀어요" % count )  # d는 문자에 상응
cost = 50000
print("나는 이번 달에 책을 %d권 샀고, 비용은 %d원 들었어요" % (count, cost))  # 뒤에 문자가 두개 이상 일 때는 두개를 괄호로 묶어 줘야 한다.

# 1인치 - 2.54cm
print("1인치는 %.2fcm입니다" % 2.54 ) # .2f를 사용하여 소수점 2번째 자리수까지만 나오게 한다.

#f 포맷방식
unit = 2.540000
print(f'1인치는 {unit:.2f}cm 입니다' )
