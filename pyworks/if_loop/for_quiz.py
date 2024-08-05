#실습1
limit = int(input("어디까지 계산할까요?"))
sum_val = 0

for i in range(0, limit+1):
    if i%2 == 1:
        sum_val += i
print(f'1부터 {limit}까지의 합: {sum_val}')

#실습2
second = int(input("몇 초?"))
for i in range(second,0,-1):
    print(i, end=" ")
print("발사!")

out = int(input("몇 단을 출력할까요?"))
for j in range(1, 10):
    print(f'{out} * {j} = {out*j}')