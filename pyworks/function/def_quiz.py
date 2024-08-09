'''
def same(x,y):
    if x == y:
        return x*y
    else:
        return x+y
print(f'결과(곱): {same(x=2, y=2)}')
print(f'결과(합): {same(x=2, y=3)}')
'''

'''
def get_price(x,y):
    if x*y < 20000:
        return (x*y)+2500
    else:
        return x*y

value1 = get_price(10000, 3)
print(f'상품1 가격: {format(value1)}원') #포멧함수를 사용하면 천단위 사용 가능

value2 = get_price(x=5000,y=3)
print(f'상품2 가격: {format(value2)}원')
'''

vending_machine = {'게토레이', '레쓰비', '생수', '이프로', '게토레이', '생수'}

def check_machine():
    print("남은 음료는", vending_machine)

def is_drink():
    if drink in vending_machine:
        return True
def add_drink():
    vending_machine.add(drink)
def remove_drink():
    vending_machine.remove(drink)

while True:
    who = input("사용자 종류를 입력하세요:\n 1.소비자\n 2.주인\n ") #\n을 하면 다음줄로 내려가짐
    if who == '1':
        drink = input("마시고 싶은 음료?")
        if is_drink():
            print(f'{drink} 드릴게요')
            remove_drink()
            check_machine()
        else:
            print(f'{drink}는 지금 없네요')
    elif who == "2":
        todo = input("할 일 선택(1.추가, 2.삭제) : ")
        print(todo)
        if todo == '1':
            check_machine()
            drink = input("추가할 음료수? ")
            add_drink()
            vending_machine.sort()  # 오름차순 정렬되면서 같은 값끼리 연결됨
            print("추가 완료")
            check_machine()

        elif todo == "2":
            check_machine()
            drink = input("삭제할 음료수?")
            if is_drink():
                remove_drink()
                print("삭제 완료")
                check_machine()
            else:
                print('없음')







