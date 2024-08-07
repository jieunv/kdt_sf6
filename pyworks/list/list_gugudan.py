# 구구단 프로그램 구현 - 리스트
# 리스트를 사용한 구구단
dan = 2
gugu = [] #빈 리스트에 구구단의 결과값 저장(2,4,6...)

for i in range(1, 10): #9까지 출력
    gugu.append([dan * i])
    print(f'{dan} X {i} = {gugu[i-1]}') #0번 인덱스를 접근해야하기 때문에 i-1을 해준다.

print("=" * 30)

# 변수에 출력된 구구단
for i in range(1, 10): #9까지 출력
    print(f'{dan} X {i} = {dan * i}')

print("=" * 30)

# 구구단 전체 출력
gugudan = []
for i in range(2,10):
    row = [] #값을 받을 빈 리스트를 하나 만든다
    for j in range(1, 10):
        row.append(i * j) #빈 리스트인 row에 추가해준다.
        print(f'{i}*{j}={row[j-1]}') #0번 인덱스를 접근(j-1)

    print() #한줄 바꿈


