'''score = int(input("점수 입력: "))
grade = "" #빈 문자열

if score >= 90:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade ="D"
else:
    grade ="E"

print(f'{grade} 등급입니다.')'''

# 연령이 20대인 경우 성별이 여성이면 "20대 여성입니다."로 출력하고 남성이면 "20대 남성입니다."로 출력
age = int(input("나이를 입력해주세요."))

if 0 <= age < 20: #0 < age < 0
    print("미성년자 입니다.")
elif age < 30:             #age >= 20 and age < 30:
    gender = input("여 or 남으로 입력해주세요.")
    if gender == "여":
        print("20대 여성입니다.")
    else:
        print("20대 남성입니다.")
elif age < 40:                    #age >= 30 and age < 40:
    print("30대 입니다.")
else:
    print("이제는 중년...")
print(f'나이는 {age}세 입니다.')