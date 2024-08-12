# 실습 1
import random

'''
list = [] # 빈 리스트 저장

for i in range(4):
    x = random.randint(1,100) #1부터 100까지의 값 중 4개를 추첨하여
    list.append(x) # 리스트에 추가한다

list.sort() # 오름차순으로 출력
print(list) # 리스트로 출력한다
'''

# 로또 번호
list = [] # 빈 리스트 저장

for i in range(6):
    x = random.randint(1,45) #1부터 45까지의 값 중 6개를 추첨하여
    list.append(x) # 리스트에 추가한다

list.sort() # 오름차순으로 출력
print(list) # 리스트로 출력한다
