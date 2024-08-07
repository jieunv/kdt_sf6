# 변수의 유효범위
# 전역변수 - 전체에 영향을 미침
# 지역변수 - 함수나 제어문 내에서만 생성되고 소멸

# 상품가격 = 단위당 가격 * 수량
def get_price():
    price = 4000 * quantity
    return price #price는 값을 주면서 사라진다(메모리에서 소멸)

def one_up(): #파이썬에서는 가능한 대문자 쓰지 말고 "_"를 사용하여 변수를 사용
    x = 0  #지역변수: 호출되면 값을 반환하고 소멸
    x += 1
    return x # x는 반환 후 계속 초기화되기 때문에 계속 1이 나온다.

print(one_up())
print(one_up())
print()

quantity = 2 #quantity는 영향을 미치는 전역변수
order_price = get_price()
print(f'{quantity}개에 {order_price}원 입니다. ')
# print(price) - 메모리에서 소멸됐기 때문에 선언되지 않았다고 뜸


