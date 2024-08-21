# 쿠폰 추첨기
# 추첨 버튼을 누르면 3명이 랜덤하게 출력됨
from tkinter import *
import random
def click():
    namelist = ['김용준','김용혁','임현수','오민선','윤종관',
                '정지은','최준영','윤다빈','박민우','조형준','고지수']

# 로또 복권 참조
#     winner = []
#     while len(winner) < 3:
#         name = random.choice(namelist) # 리스트에서 3명을 추출
#         if name not in winner:
#             winner.append(name)

# set() 자료구조 구현
    winner = set()
    while len(winner) < 3:
        name = random.choice(namelist) # 리스트에서 3명을 추출
        winner.add(name)

    text.delete(0.0,END)
    text.insert(END,winner)

window = Tk()
window.title('쿠폰 추첨기')

lbl_img = Label(window)
# 이미지 객체 생성
img = PhotoImage(file='bronx.png')
# 이미지 넣기 - Lable에 이미지 넣음
lbl_img.config(image=img)
lbl_img.grid(row=0, column=0, sticky=W)

# 추첨 버튼
Button(window, text="추첨", command=click).grid(row=1, column=0, sticky=E)

# 출력 상자(이름)
text = Text(window, width=47, height=3, bg='yellow')
text.grid(row=2, column=0, sticky=W)

window.mainloop()