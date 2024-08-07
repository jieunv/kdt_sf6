#함수는 재사용이 가능한 코드 블럭
print("Hello~")

# 인사하는 함수 - greet
# 지역 영역
def greet():
    print("안녕~ ") # def 안에서는 print()를 사용해도 출력되지 않는다

# 인사하며 이름까지 부르는 함수 - greeting
def greeting(name): #name은 변수
    print("안녕~", name)

def get_gugu(dan):
    for i in range(1,10):
        print(f'{dan} X {i} = {dan * i}' )
# 메인 영역
greet() #사용자가 정의한 greet() 함수를 호출해야 출려된다.
greeting("지은") # name == '지은'
greeting("민선") # name == '민선'


# 구구단 호출
get_gugu(4)

def add(x, y):
    total = x + y
    print("더하기: ", total)

# 더하기 호출
add(x=10,y=11)


