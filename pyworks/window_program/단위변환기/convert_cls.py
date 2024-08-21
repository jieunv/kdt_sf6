# 클래스 샘플 - 객체를 생성해서 버튼 이벤트 구현

from tkinter import * # 모든 모듈이나 함수를 사용
from scale_converter import ScaleConverter

class App:
    def __init__(self, root):
        self.conv = ScaleConverter('KB', 'MB',1024)
        frame = Frame(root)
        frame.pack()  # 한 줄을 꽉 채움(가운데 정렬)
        Label(frame, text="KB").grid(row=0, column=0)
        self.kb = IntVar()
        # textvariable = 객체(멤버) 변수, "KB" 입력
        Entry(frame, textvariable=self.kb).grid(row=0, column=1)

        # "MB" 출력 - 레이블
        Label(frame, text="MB").grid(row=1, column=0)
        # 'MB' 출력 - 레이블. 실수형 클래스 - DoubleVar()
        self.mb = DoubleVar()
        Label(frame, textvariable=self.mb).grid(row=1, column=1)

        Button(frame, text="변환", command=self.convert).grid(row=2, column=2)

    def convert(self):
        kb = (self.kb.get())
        mb = self.conv.convert(kb)
        mb = f'{mb:.2f}'
        self.mb.set(mb)

root = Tk()
root.title("단위 변환기")
root.geometry('300x150+200+200')



app = App(root) #클래스 객체 생성 - root를 인자로 생성
root.mainloop()


















'''class App:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        Label(frame, text="KB").grid(row=0, column=0)
        Button(frame, text="변환", command=self.convert).grid(row=1,column=0)
    def convert(self):
        print("Not Implemented")

root = Tk()
root.title("단위 변환기")
root.geometry("250X100+200+200")

app = App(root)

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.unit_from = units_from
        self.unit_to = units_to
        self.factor = factor
'''


