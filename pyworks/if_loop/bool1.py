# 비교 연산 - >, >=, <, <=, ==(같다), !=(같지 않다)
#비교 연산의 결과는 - bool자료(True/False)
b1 = 2> 1
print(b1) # True
print(type(b1))

b2 = (2 == 1)
print(b2)

b3 = (2 != 1)
print(b3)


#논리 연산 - and, or, not
logic1 = (2 > 1) and (2 == 1) # and 연산은 2가지 이상의 조건에서 모두 참일 때만 참이다.(False)
print(logic1)

logic2 = (2 > 1) or (2 == 1) # or 연산은 2가지 이상의 조건에서 하나만 참이어도 참이다.(True)
print(logic2)

logic3 = not (2 != 1) # not 연산은 부정(False)
print(logic3)

# 논리 연산 예제
age = 17
under_20 = age < 20

print(under_20)
print(not under_20)

#논리곱 - 양쪽 다 참이어야 True
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

#논리합 - 양쪽 중 한쪽만 참이어도 True
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False)  #False

#논리 부정
print(not True) #False
print(not False) #True
