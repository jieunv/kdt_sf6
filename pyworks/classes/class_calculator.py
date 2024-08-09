class Calculator:
    def __init__(self): #생성자 입력
        self.x = 0 #멤버변수, 인스턴스 변수(지역변수)
        # self.y = 0

    # 클래스의 메서드
    def add(self, y):
        self.x += y # 기존에 있던 x에 y를 더한다
        return self.x

    # sub() 매서드 생성
    def sub(self,y):
        self.x -= y
        return self.x

c1 = Calculator() #생성자에서 선언한게 없어 넣을게 없기 때문에 () 안에 아무말도 넣지 않는다
print(c1.x)
print(c1.add(10)) #10 = 매개값, y값에 10을 넣어준다.
print(c1.sub(5))

