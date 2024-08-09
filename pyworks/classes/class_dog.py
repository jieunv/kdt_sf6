# 클래스 변수는 값을 공유하고 유지하는 속성이 있고
# 클래스 이름으로 직접 접근한다

class Dog:
    kind = "진돗개"   # 클래스 안에 있다고 하여 "클래스 변수"
    def __init__(self,name): #생성자 입력
        self.name = name # "인스턴스 변수" - self를 통해 내부와 외부를 구별해주며 외부에서 입력하면 내부로 입력된다.
# 객체(인스턴스) 생성
dog1 = Dog("송이") #dog1, dog2는 인스턴스(객체) 변수
dog2 = Dog("백구")

'''
print(dog1.name) 
print(dog2.name) 
# 클래스 변수는 이렇게 사용하지 않음 인스턴스(객체) 변수는 이렇게 사용함
print(dog1.kind)
print(dog2.kind)
'''
# 클래스 변수는 클래스 이름으로 접근
print(Dog.kind)

# 객체 리스트
dogs = [
    Dog('멍이'),
    Dog('해피'),
    Dog('사랑이')
]

# 리스트 출력 시엔 for문을 사용한다.
for dog in dogs:
    print(dog.name)
