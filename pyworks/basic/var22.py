#소수점 처리하기
n1 = 10
n2 = 3

div = n1 / n2
print(type(n1))
print(type(div))

print(f'결과값: {div : .2f}')
print(f'결과값: {round(div, 2)}')


#반올림 함수 - round(숫자. 자리수)
print(round(1.647, 2))

#실습 - 빵 30개, 사람 4명

bread = 30
people = 4

몫 = bread // people #한글 변수 가능
나머지 = bread % people

print("빵의 개수: " + str(몫)) 
print("남은 빵의 개수: " + str(나머지))
