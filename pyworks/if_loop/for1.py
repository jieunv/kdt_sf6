# for 반복문
'''
for i range(시작값, 종료값(값에서 1을 뺀 값으로 생각해야됨), 증감값):
    실행문
for in list:
    실행문
'''

# 초기값이 생략되면 0부터 시작
# 끝값은 실제(끝값 -1임)
# 세번째 인자 - 증감값(step)
a = range(10)
print(list(a)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = range(1, 11)
print(list(b)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = range(1, 11, 2)
print(list(c)) #[1, 3, 5, 7, 9]

'''
#for문 - 1부터 10까지 출력
for i in range(1,11):
    print(i, end=" ")
'''

#for - 1부터 10까지 더하기(합계)
total = 0 #초기값을 미리 정해야됨(초기화 시킴 0으로 저장) - 합계 저장 변수는 영어로 작성
for i in range(1,11):
    total += i
    print("i =", i, "total = ", total)
print(total)

