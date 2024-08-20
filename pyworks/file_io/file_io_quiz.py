# 실습 1 - 구구단

'''
f = open("c:/pyfile/gugudan.txt", "a")

for i in range(2, 10):
    for j in range(1,10):
        f.write(f'{i} X {j} = {i*j}\n')
    f.write('\n') #단과 단 사이를 한 칸 띄우고 싶을 때
f.close()

f = open("c:/pyfile/gugudan.txt", "r")

gugu = f.read()
print(gugu)
f.close()


# 실습2
try:
    with open("./source/member.txt", 'w') as f:
        for text in range(3):
            name = input("이름을 입력하세요 : ")
            pw = input("비밀번호를 입력하세요 : ")
            f.write(f'{name} {pw}\n')

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
'''

# 실습 3
# 로그인

name = input('이름 입력: ')
pw = input('비밀번호 입력: ')
user = name + " " + pw + '\n'

with open("./source/member.txt", 'r') as f:
    member_list = f.readlines()
    print(member_list)

    # 상태 변수 - True/False
    sw = False
    for member in member_list:  # 리스트를 순회하면서
        if member == user:      # 파일에 있는 member의 name, pw와 입력한 user의 name, pw가 일치하면
            sw = True           # 상태를 True로 저장

    if sw:      #sw == True
        print("로그인 성공!")
    else:       #sw == False
        print("로그인 실패!")



