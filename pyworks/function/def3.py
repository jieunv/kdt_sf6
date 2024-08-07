# 1부터 n까지 곱하는 함수
def gob_n(n):
    gob_v = 1 #sum_v는 초기값을 0으로 해야하지만 곱하기는 초기값을 1로 선정해야한다
    for i in range(1,n+1): #5-1인 4까지 출력한다
        gob_v *= i
    return gob_v

"""
        출력결과
    i = 1  1 = 1 * 1
    i = 2  2 = 1 * 2
    i = 3  6 = 2 * 3
    i = 4  24 = 6 * 4 
출력결과 4! = 4 * 3 * 2 * 1 과 같은 값을 가진다.
"""
# print("결과값 : ", gob_v())

print("결과값 : ", gob_n(4)) #return을 안해주면 None 출력
print("결과값 : ", gob_n(10))