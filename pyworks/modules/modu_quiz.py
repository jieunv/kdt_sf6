# 실습 1
import random

list1 = [] # 빈 리스트 저장

for i in range(4):
    x = random.randint(1,100) #1부터 100까지의 값 중 4개를 추첨하여
    list.append(x) # 리스트에 추가한다

list.sort() # 오름차순으로 출력
print(list1) # 리스트로 출력한다


# 실습2 - 로또 번호1
list2 = [] # 빈 리스트 저장

for i in range(6):
    x = random.randint(1,45) # 1부터 45까지의 값 중 6개를 추첨하여
    list2.append(x) # 리스트에 추가한다
    no_list = list(set(list2)) # 중복 없이 출력

list2.sort()  # 오름차순으로 출력
print(no_list)  # 리스트로 출력한다

# 실습2 - 로또 번호2
list3 = [] # 빈 리스트 저장

'''
for i in range(6):
    print(len(list2))
    x = random.randint(1,45) #1부터 45까지의 값 중 6개를 추첨하여
    if x not in list2:  # 중복 없이 출력
        list2.append(x) # 리스트에 추가한다
'''

while len(list3) < 6:
    print(len(list3))
    x = random.randint(1, 45)  # 1부터 45까지의 값 중 6개를 추첨하여
    if x not in list3:  # 중복 없이 출력
        list3.append(x)  # 리스트에 추가한다

list3.sort()  # 오름차순으로 출력
print(list3)  # 리스트로 출력한다




