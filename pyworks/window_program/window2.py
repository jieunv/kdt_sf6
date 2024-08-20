# 윈도우 생성 - tkinter
# 체계: root=TK() > Frame() > Label(), Button()
# import tkinter as tk # as tk라고 써서 별칭을 만듦
from tkinter import *
# 루트 생성
root = Tk()
root.title("처음 만드는 윈도우")
# 창 크기(가로x세로)
root.geometry("300x100")

# 콤포넌트(구성요소 - 레이블, 버튼, 입력 상자)
# 출력(Lable)
# 배치-pack(): 한줄을 차지(LEFT, RIGHT, TOP, BOTTOM)
# grid(): 자유롭게 배치(E, W, S, N)
# Label(root, text="안녕하세요~") .grid(row=0, column=0)
Label(root, text="안녕하세요~") .grid(row=0, column=0)
Button(root, text="확인").grid(row=1, column=1, sticky=E)


root.mainloop()