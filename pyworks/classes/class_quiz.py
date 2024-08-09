'''# 실습1 - 사칙연산 클래스 만들기
import sys
class Calculator:
    # 생성자 메서드(함수)
    def __init__(self, x, y): #생성자 입력
        self.x = x # 내부와 외부값의 기호를 가독성 있게하려고 self를 붙임
        self.y = y

    # add() 매서드 생성
    def add(self):
        return self.x + self.y

    # sub() 매서드 생성
    def sub(self):
        return self.x - self.y

    # mul() 매서드 생성
    def mul(self):
        return self.x * self.y

    # div() 매서드 생성
    def div(self):
        if self.y == 0:
            print("0으로 나눌 수 없음")
            return sys.exit(0)
        else:
            return self.x / self.y

c1 = Calculator(10,2)
print(c1.add())
print(c1.sub())
print(c1.mul())
print(c1.div())
'''

# 실습2. 슈퍼마켓 클래스

class Supermarket:
    a = []
    def __init__(self,location,name,product,customer):
        self.location = location #위치
        self.name = name # 가게 이름
        self.product = product # 파는 물건
        self.customer = customer # 고객의 수

    def print_location(self, location):
        print(f'위치: {self.location}')

    def chang_category(self, another_product):
        self.product = another_product

    def show_list(self):
        print(f'상품: {self.location}')

    def enter_customer(self):
        self.customer += 1

    def show_info(self):
        print(f'위치: {self.location}, 이름: {self.name},' 
              f'상품: {self.product}, 고객수: {self.customer}')

super1 = Supermarket("마포구 염리동", "마켓온", "음료",10)
super1.print_location()
super1.chang_category("음료")
super1.show_list()
super1.enter_customer() #고객1 들어옴
super1.enter_customer() #고객1 들어옴
super1.show_info()

