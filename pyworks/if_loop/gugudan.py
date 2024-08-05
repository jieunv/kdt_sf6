#구구단 3단
'''
 3 X 1 = 3
 3 X 2 = 6
 ...
 3 X 3 = 9
 3 X 4 = 12
 3 X 5 = 15
'''
dan = int(input("몇 단을 출력할까요?"))
for i in range(1, 10):
    print(f'{dan} X {i} = {dan*i}')

#구구단 전체 코드
dan = int(input("몇 단을 출력할까요?"))
for i in range(2, 10):
    for j in range(1,10):
        print(f'{i} X {j} = {i*j}')

