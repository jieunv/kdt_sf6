# while True: 무한 반복문 - if ~ break(빠져나옴)

'''
while True:
    lunch = input("오늘 점심 메뉴?")
    if lunch == "그만":
        break
    print(lunch + "!!")
print("Done")
'''

# 1부터 10까지 출력하기
count = 0
while True:
    count += 1

    if count > 10:
        break
    print(count, end=" ") #end=""를 사용하여 공백을 주면 엔터 없이 한줄로 출력이 가능하다.
print("끝")