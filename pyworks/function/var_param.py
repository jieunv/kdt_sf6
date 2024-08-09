# 가변 매개변수
# 매개변수의 입력값이 정해지지 않은 변수임
# 변수 이름 앞에 접두어 '*'를 붙인다.

def calc_avg(*numbers): # [1, 2]
    sum_v = 0 #초기화
    for i in numbers:
        sum_v += i #하나씩 더해진다
    return sum_v / len(numbers) # 합계 / 개수 = average(평균)

avg1 = calc_avg(1,2) #매개 변수가 2개
print(avg1)

avg2 = calc_avg(1,2,3,4) #매개 변수가 2개
print(avg2)