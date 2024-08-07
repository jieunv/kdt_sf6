# 1차원 리스트의 합계와 평균

a = [1, 2, 3, 4]

total = 0
for i in a:
    total += i

print("합계 = ", total)
print("평균 = ", total / len(a)) #1차원 리스트만 len() 함수 사용이 가능하다

# 2차원 리스트의 합계와 평균

d = [
    [1],
    [2,3],
    [4,5,6]
]

sum_v = 0 # 아래에 있는 sum_v += d[i][j] 코드를 사용해야하기 때문에 변수 설정을 해두어야한다. 없으면 error
count = 0
for i in range(len(d)): #행의 개수이기 때문에 전체 개수가 아니다.
    for j in range(len(d[i])):
        sum_v += d[i][j]
        count += 1 # 한 번 계산될 때 카운트도 하나씩 늘어나기 때문에 입력해준다 / 파이썬 외 다른 툴에서는 ++;을 사용한다.

'''
    1 = 0 + 1 -- [0][0] count = 1 # 계산은 계산대로 진행되고 카운트는 카운트 대로 증가된다.
    3 = 1 + 2 -- [1][0] count = 2
    6 = 3 + 3 -- [1][1] count = 3

'''

print("요소의 개수 = ", count)
print("합계 = ", sum_v)
# print("평균 = ", sum_v / len(d)) - len()은 행의 개수이기에 2차원 함수에서는 사용 불가
print("합계 = ", sum_v / count)


