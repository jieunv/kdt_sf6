# 인스턴스 변수와 클래스 변수

class Dog:
    tricks = [] # 클래스변수(요소가 초기화되지 않고 유지) - 클래스 이름으로 접근

    def __init__(self,name):
        self.name = name
        #self.tricks = [] # 이건 인스턴스 변수(self 입력 필수) - 결과값이 유지되는 것이 아닌 초기화됨
        # print("생성자 메서드입니다.")
    # 출력결과
        # 생성자 메서드입니다.
        # ['몸 뒤집기']
        # 생성자 메서드입니다.
        # ['죽은척 하기']

    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog('존')
dog1.add_trick("몸 뒤집기")
# print(dog1.tricks) # 인스턴스 변수 출력값
print(Dog.tricks) # 클래스 변수 출력값 - 클래스 이름으로 접근

# 앞에 dog1 결과값에 더해져서 출력된다
dog2 = Dog('제리')
dog2.add_trick("죽은척 하기")
print(dog2.tricks) # ['몸 뒤집기', '죽은척 하기']

