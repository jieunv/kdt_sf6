from tkinter import *

def click():
    # print("안녕! 파이썬")
    label.config(text="안녕~ 파이썬")
root = Tk()
root.title("윈도우3")
root.geometry("250x150") # 창크기
root.option_add("*Font", "맑은고딕 15")

frame = Frame(root)
frame.pack()

Label(frame, text="Hello~ Python!!").grid(row=0, column=0)
# command 속성: 버튼 눌렀을 때 함수를 실행
# click() 함수를 쓰지만 함수 생성시점이 아닌 클릭했을 때 실행되어야 하기때문에 ()를 뺀다
Button(frame, text="확인", command=click).grid(row=1, column=0)
# 출력 레이블
label = Label(frame, text="")
label.grid(row=2, column=0)


root.mainloop()