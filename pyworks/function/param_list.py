# 리스트를 매개변수로 사용하는 함수
def times(a):  # v와 다른 문자를 넣어도 상관없음 # a = [1,2,3,4]
    a2 = []  # 배수를 저장할 빈 리스트 선언(생성)
    for i in a:
        a2.append(i * 4)

'''    a2 = [ i * 3 for i in a ]
    if a2 // 3 == 0:
        return a2
'''
v = [1,2,3,4]
v2 = times(v)  #호출 3의 배수
print(v2)

# 실습문제 - 3의 배수 구하고 출력하기
def times(a):  # v와 다른 문자를 넣어도 상관없음 # a = [1,2,3,4]
    count = 0  # 지역 변수
    a2 = []  # 배수를 저장할 빈 리스트 선언(생성)
    for i in range(1, 31):
        if (i % a == 0):
            print(i, end=" ")
            count += 1
    print(f' 3의 배수의 개수: {count}')
times(3)
