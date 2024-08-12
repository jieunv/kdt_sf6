# 수학 관련 내장 모듈 _ math 사용

import math

print(math.pi)

# 원의 넓이(area)
radius = 6
area = radius * radius * math.pi
print(area)

# 올림 - 1을 더해서 정수로 반환
print(math.ceil(2.45))
print()

# 버림(내림) - 소수점 이하를 버리고 정수로 반환
print(math.floor(2.45))

# 제곱근(루트) - 제곱근으로 실수로 반환
print(math.sqrt(25))

# 반올림(내장함수) - round()
print(round(2.57, 1)) # 출력할 자릿수를 입력한다. 이 코드의 경우 첫 번째 자리까지 반올림되어 나타난다.
