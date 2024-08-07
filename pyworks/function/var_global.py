# global - 전역변수임을 알려주는 키워드, 값을 유지하고 공유함
# 전역변수는 지역이나 제어문에 영향을 미침, 프로그램이 종료되면 소멸

def one_up():
    global x #global을 사용함으로써 전역변수로 선언한다
    x += 1
    return x

x = 0
print(one_up()) #1
print(one_up()) #2
print(one_up()) #3
print("x = ", x) #x가 전역변수가되면서 소멸되지 않아 x의 값이 증가한다.