# 모듈(module) 불러오기
from classes.class_quiz import Calculator
import sys
# 객체 생성
calc = Calculator(4, 5)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())

# Calculator 상속받기
class MoreCaculator(Calculator):
    # 거듭 제곱 계산 기능 추가
    def pow(self):
        return self.x ** self.y
    def div(self):
        try:
            # return self.x / self.y
            super().div()
        except:
            print("0으로 나눌 수 없습니다.")
            sys.exit(0)

mc = MoreCaculator(6, 0)
print(mc.add())
print(mc.pow())
print(mc.div())