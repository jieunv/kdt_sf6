# 학생 5명의 국어, 수학의 총점과 평균 계산
# 개인 점수를 구할 땐 2중포 대신 단일로 사용한다

# 5명이 2과목이기 때문에 5행에 2열로 리스트를 생성한다
score = [
    [80, 70],
    [70, 95],
    [60, 90],
    [50, 75],
    [75, 60]
]

# 개인별 총점과 평균
# 개인별 총점을 저장
total = 0 #total = score[i][0] + score[i][1] 에서 사용하기 때문에 total 변수 설정을 하지 않아도 에러가 뜨지 않는다
students = [] # 빈 리스트를 만든다
n = len(score)
print("총점 평균")
for i in range(0, n): #행의 개수를 쓸 때는 사용 가능하다
    # 총점 = 국어 점수 + 수학 점수
    # total(지역변수)은 필요한 곳에서 선언(생성)해서 사용
    # 코드 블럭을 빠져나올 때 소멸되기 때문에 소멸된 후에 리스트에 total을 추가해준다
    total = score[i][0] + score[i][1]
    students.append(total)

    print(total, total / 2) # 모두 다 2과목이기 때문에 따로 변수를 사용하지 않는다
print(students)

# 과목별 총점과 평균
# 국어 총점, 수학 총점, 국어 평균, 수학 평균
# 행과 열이 있기에 이중 for가 아닌 단일 for로 가능하다

# sum_kor = 0, sum_math = 0 이런식으로 변수를 저장해도 되지만 변수의 개수가 늘어나고 사용이 번거로워진다.
sum_subject = [0, 0] #국어 총점, 수학 총점 - 빈 리스트 제공, 인덱스로 표현하기 때문에 간결하다.
avg_subject = [0.0, 0.0] #국어 평균, 수학 평균 - 자리수를 미리 지정해준다.

for i in range(0, n): # n = len(score) - 단일 for를 사용하고 행의 개수를 쓰기 때문에 len() 함수 사용이 가능하다.
    sum_subject[0] += score[i][0] # score 내에 리스트에 있는 0번(국어 점수)을 모두 더한다
    sum_subject[1] += score[i][1] # score 내에 리스트에 있는 1번(수학 점수)을 모두 더한다

# 평균 계산
avg_subject[0] = sum_subject[0] / n # n = len(score)
avg_subject[1] = sum_subject[1] / n # n = len(score)

print(f'국어 총점: {sum_subject[0]}')
print(f'수학 총점: {sum_subject[1]}')
print(f'국어 평균: {avg_subject[0]}')
print(f'수학 평균: {avg_subject[1]}')

