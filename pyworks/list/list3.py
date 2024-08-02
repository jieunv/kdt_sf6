my_shop = ["반팔티", "청바지", "이어폰",['무선키보드', '유선키보드']] # 리스트 안에 리스트가 있을 경우 리스트는 하나의 행으로 여겨진다.

# 이어폰을 출력하기
print(my_shop[2])

# 반팔티를 긴팔티로 수정
my_shop[0] = "긴팔티"
print(my_shop[:])

print(my_shop[3])
print(my_shop[-1])

print(my_shop[3][0]) # 리스트 안에 리스트가 있을 경우에 첫번째 리스트의 3번째 자리수에 있는 리스트 안에 0번째 자리수가 출력된다.
print(my_shop[3][1])

# 여러개 삭제할 때
del my_shop[0:2]  #0번 1번 동시에 삭제

print(my_shop)