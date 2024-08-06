 # 실습4
age = int(input("나이를 숫자로 입력해 주세요: "))
payment = input("결제 방법을 입력해주세요. ('카드' 또는 '현금'만 입력): ")

fee = "" # 빈문자열

if payment == "카드":
    if age < 8:
        fee = "무료"
    elif age < 14:
        fee = "450"
    elif age < 20:
        fee = "720"
    elif age < 75:
        fee = "1200"
    else:
        fee = "무료"
else:
    if age < 20:
        fee = "1000"
    else:
        fee = "1300"

print(f'{age}세의 {payment}요금은 {fee}원 입니다.')