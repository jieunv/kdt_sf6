# 파일 쓰기 - 파일을 생성
# 파일 열기(open()) > 파일 쓰기(write()) > 종료(close())
# 절대 경로(c:/디렉터리/파일), 상대 경로
# 모드(mode) - 쓰기모드('w'), 읽기모드('r'), 추가모드('a')
# 문자(글자)를 쓰기(저장)

f = open("c:/pyfile/file1.txt", "w")  #(파일 경로, 모드)

# 한번 내용을
f.write("Hello~ Python\n")
f.write("너무 더워!!!\n")
# f.write("한자\n") - 한자도 입력 가능
# 숫자 저장 - 문자로 저장됨
f.write('100\n')
f.write("16.7\n")
f.close()

