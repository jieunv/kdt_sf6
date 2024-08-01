# 입력함수 - input(문자열)

"""
name = input("이름 입력: ") #무언가를 입력할 수 있도록 만들어놓음
print("당신의 이름은 " + name + "이군요")

number = input("숫자 입력: ")
print(number)
print(number + 1)

#오류처리(try ~ except)
num1 = int(input("첫번째 수 입력: "))
num2 = int(input("두번째 수 입력: "))
print(type(num1)) #int
print(num1+num2)

"""

int_num = print(10.5)
print(int_num)

print(int(10.5))

#오류처리(try~except 구문)
# :(콜론) - 코드블럭({})
# 다음 줄에서는 4칸 띄어쓰기(indent)
try:
    실행문(오류가 나올 수 있는 문)
    
except:
    오휴를 처리할 수 있는 구문
try:
    num1 = input("첫번째 수 입력: ")
    num2 = input("두번째 수 입력: ")
    print(int(num1)+int(num2))
except:   
    print("정수를 입력해주세요")




