'''# 과제1. 자판기 프로그램
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
        '''

# 과제2
vending_machine = ['게토레이', '레쓰비', '생수', '이프로', '게토레이', '생수']

while True:
    print('=' * 20, "RESTART")
    who = input("사용자 종류를 입력하세요:\n 1.소비자\n 2.주인\n ") #\n을 하면 다음줄로 내려가짐
    if who == '1':
        drink = input("마시고 싶은 음료?")
        if drink in vending_machine:
            vending_machine.remove(drink)  # 입력된 drink 삭제
            print(f'{drink} 드릴게요')
            print(f'남은 음료는 {vending_machine}입니다.')
        else:
            print(f'{drink}는 지금 없네요')
    elif who == "2":
        todo = input("할 일 선택(1.추가, 2.삭제) : ")
        if todo == '1':
            print("남은 음료는", vending_machine)
            drink = input("추가할 음료수?")
            vending_machine.append(drink) #drink 추가
            vending_machine.sort() #오름차순 정렬
            print("추가 완료")
            print("남은 음료는", vending_machine)

        elif todo == "2":
            print("남은 음료는", vending_machine)
            drink = input("삭제할 음료수?")
            if drink in vending_machine:
                vending_machine.remove(drink)  # drink 삭제
                print("삭제 완료")
                print("남은 음료는", vending_machine)
            else:
                print('없음')

