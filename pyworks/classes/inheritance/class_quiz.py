# 실습3
class Calculator:
    def __init__(self):
        self.value = 100

    def sub(self, value):
        self.value -= value
        return self.value

lc = Calculator()
print(lc.sub(20))
print(lc.sub(90))

class LimitCalculator(Calculator):
        def sub(self, value):
            # self.value -= value
            super().sub(value)
            if self.value < 0:
                 self.value = 0
            return self.value

# 실행코드
lc = LimitCalculator()
print(lc.sub(20))
print(lc.sub(90))
