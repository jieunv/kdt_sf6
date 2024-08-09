# 재귀함수 - 자기 자신을 호출하는 함수

'''
# 일반 함수 출력법
def sos(i):
    for a in range(i):
        print("Help me!!")
sos(5)
'''

def sos(i):
    print("Help me!!")
    if i == 1:
        return ""
    else:
        return sos(i-1)
sos(5)

"""
sos(5)
n = 5, Help me!!

sos(4)
n = 4, Help me!!

sos(3)
n = 3, Help me!!

sos(2)
n = 2, Help me!!

sos(1)
n = 1, Help me!!
"""

# 팩토리얼 계산
# 종료 조건을 충분히 작야야 함
def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n-1)

'''
    4! = 4 * (4-1)!
    3! = 3 * (3-1)!
    2! = 2 * (2-1)!
'''

print(facto(4))