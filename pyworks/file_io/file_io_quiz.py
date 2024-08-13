# 실습 1 - 구구단

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