import datetime
# 현재(오늘) 날짜와 시간 모두 출력
# now = datetime.datetime.now() - now, today 모두 다 사용 가능
now = datetime.datetime.today()
print(now)

print(now.year)     #년도
print(now.month)    #월
print(now.day)      #일

# 날짜만 출력
print(f'{now.year}-{now.month}-{now.day}')

# 시간만 출력
print(f'{now.hour}:{now.minute}:{now.second}')

# 특정 날짜 출력 - 2023년 7월 31일
the_day = datetime.date(2024, 7, 31)
print(the_day)

# 오늘 날짜만 출력
today = datetime.date.today()
print(today)

# D+day 구하기
print(" ★ 지금까지 몇 일? ★ ")
passed_time = today - the_day
# print(passed_time)
print(f'개강 이후 {passed_time.days}일 지났습니다.')

# D-day 구하기
print(" ★ 추석까지 몇 일? ★ ")
chusuk = datetime.date(2024, 9,17)
d_day = chusuk - today
print(f'추석까지 {d_day.days}일 남았습니다.')

