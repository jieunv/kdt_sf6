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
'''

# 실습2
try:
    with open("./source/member.txt", 'w') as f:
        for text in range(3):
            name = input("이름을 입력하세요 : ")
            pw = input("비밀번호를 입력하세요 : ")
            f.write(f'{name} {pw}\n')

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")


# 실습 3

