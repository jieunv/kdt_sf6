#전체 구구단(중첩 for문)
for i in range(1,5): # i =1,2,3,4
    for j in range(1,5): # j =1,2,3,4
        print("가", end="")
    print() #행바꿈



'''i = 1
   j = 1,        가 
   j = 2,        가가
   j = 3,        가가가
   j = 4,        가가가가
i =2
   j = '''


for i in range(1,5): # i =1,2,3,4
    for j in range(1,5): # j =1,2,3,4
        print("*", end="")
    print() #행바꿈


for i in range(1,5): # i =1,2,3,4 #행
    for j in range(1,6-i): # j =1,2,3,4 #열

        print("*", end="")
    print() #행바꿈

print("="*30) #구분선
print('=' * 20) #구분선

# 파이썬의 단일 for
for i in range(1,5): #행은 4행까지 나온다.
    print('*' * i)
'''
*
**
***
****
'''

print("="*20)

# 거꾸로 출력하기
for i in range(1,5): #행은 4행까지 나온다.
    print('*' * (5-i))
'''
****
***
**
*
'''

#공백문자 나오게 하기
for i in range(1,5): #행은 4행까지 나온다.
    print( " " * (4-i) + '*' * i)
'''
   *
  **
 ***
****
'''

#숫자가 연속으로 증가하는 알고리즘
for i in range(0,4):
    for j in range(1,5):
        num = i * 4 + j
        print(num, end=" ")
    print()

# 4의 배수 + 1~4 더함

'''
1 2 3 4 
5 6 7 8  
9 10 11 12
13 14 15 16 
'''

#숫자가 연속으로 증가하는 알고리즘(일정 수까지만 출력하고 싶을 때)
for i in range(0,4):
    for j in range(1,5):
        num = i * 4 + j
        if num > 15: # num이 15보다 커지면 빠져나오도록 한다.
            break
        print(num, end=" ")
    print()

# 4의 배수 + 1~4 더함

'''
1 2 3 4 
5 6 7 8  
9 10 11 12
13 14 15
'''

