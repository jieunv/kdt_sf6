# 카운터 만들기 - 클래스 변수
class Counter:
    x = 0 # 클래스 변수
    def __init__(self):
        self.x + 1
        Counter.x += 1 #카운터로 직접 접근 해야함, 생성될 때마다 (전 결과값+1)

c1 = Counter()
print(Counter.x) #1

c2 = Counter()
print(Counter.x) #2

c3 = Counter()
print(Counter.x) #3

class Counter2:
    def __init__(self): # 인스턴스 변수
        self.x = 0 # 생성될 때마다 여기서 초기화됨
        self.x += 1

count1 = Counter2()
print(count1.x) #1

count2 = Counter2()
print(count2.x) #1

count3 = Counter2()
print(count3.x) #1