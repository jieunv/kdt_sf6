# 실습1
# 조건 - 시내에서 자동차의 주행속도가 50Km 이상이면 "속도위반 입니다"를 출력하고
# 아니면 "규정속도 준수!"를 출력하세요

limit_speed = float(input("주행속도를 입력해주세요: "))
if limit_speed >= 50:
    print("속도위반 입니다.")
else:
    print("규정속도 준수!")
print(f'주행속도는 {limit_speed}km입니다.')