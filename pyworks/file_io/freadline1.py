# readline() - 한 줄 읽기(첫번째 줄)
# readlines() - 전체 줄을 읽고 리스트로 반환

f = open("c:/pyfile/file1.txt", "r")
# print(f.read())

# 한 줄 읽기
Line1 = f.readline()
print(Line1)

# 한 줄씩 전체 읽기
while True:
    line = f.readline()
    if not line:
        break
    print(line.strip()) # strip() 공백 제거

f.close()