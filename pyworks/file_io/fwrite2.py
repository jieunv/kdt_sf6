# 입력받아서 파일 쓰기 - 추가 모드

f = open("c:/pyfile.inputput.txt,", 'a')
# 숫자 저장
# f.write(100) #TypeError
# 계산 결과 변수를 쓰면 저장됨
num = 4 + 5
f.write(f'{num}\n')
f.write('str(num) + \n')
f.write("100\n") # 숫자 입력 가능
f.write("15.9\n") # 실수 입력 가능
text = input("글자입력: ")
f.write(text)
f.write("\n")
f.Close()