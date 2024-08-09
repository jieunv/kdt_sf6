# 정보은닉(Information Hiding)
class Health:
    def __init__(self, name): # 생성자에 넣으면 set이 불필요 - get, set은 꼭 함께 써야하는 것x
        self.__name = name
        self.__hp = 100 # 기본적 100으로 초기화함

    def getname(self): #p1 = Health("나몸짱") 여기에 set 입력이 되어있기 때문에 따로 set은 입력하지 않는다
        return self.__name

    def sethp(self, hp):
        if hp < 0:
            hp = 0 # 범위 제한 - 0보다 작으면 0으로, 100보다 크면 100으로 설정한다
        elif hp > 100:
            hp = 100
        self.__hp = hp

    def gethp(self):
        return "hp: " + str(self.__hp) # 문자로 맞춰주기 위해 앞에 str을 사용한다

    def exercise(self, hours):
        self.sethp(self.__hp + hours)
        print("{}시간 운동하다".format(hours))
        # print(f'{hours}시간 운동하다')
        print("sky".format()) #문자열 지원

    def drink(self, cups):
        self.sethp(self.__hp - cups)
        print("술을 {0}잔 마시다".format(cups))

p1 = Health("나몸짱") # 여기에 내용을 넣으면 set이 된다. 즉 위에서 따로 set 언급을 하지 않아도됨
p1.sethp(100)
p1.exercise(3)
print(f'{p1.getname()} - {p1.gethp()}')

p2 = Health("한잔해")
p2.sethp(0)
p2.drink(4) # 계산하면 -4가 나오지만 위에서 범위제한을 해두었기에 0이 출력된다
print(f'{p2.getname()} - {p2.gethp()}')

