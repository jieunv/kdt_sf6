# 과제1. 자판기 프로그램
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']

while True:
    print('=' * 20, "RESTART")
    drink = input("마시고 싶은 음료?")
    if drink in vending_machine:
        vending_machine.remove(drink) #입력된 drink 삭제
        print(f'{drink} 드릴게요')
        print(f'남은 음료는 {vending_machine}입니다.')
    else:
        print(f'{drink}는 지금 없네요')
