# 파일 읽기 - 기존의 파일의 내용을 읽기
# 파일 열기(open()) > 파일 쓰기(write()) > 종료(close())

f = open("c:/pyfile/file1_txt", "r")

print(f.read())
data = f.read()
print(data)
f.close()