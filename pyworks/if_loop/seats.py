#자리배치도
# 고객수 - customer, 좌석열 - column, 행 - row
# 나머지가 0일 때 행의 수, 0이 아닐 때 행의수

customer = int(input("고객수를 입력하세요: "))
column = int(input("좌석열 수룰 입력하세요: "))

if customer % column == 0:
    row = customer // column
else:
    row = customer // column + 1
print(row)

for i in range(0,row):
    for j in range(1, column + 1):
        seat = i * column + j
        if seat > customer:
            break
        print(seat, end=" ")
    print()

