# 리스트(배열) - 같은 유형의 연속 적인 값을 저장할 때 사용 하는 자료 구조
# 인덱싱 : 순서가 있고 0번 위치 부터 시작
# 리스트 생성 시 -  1. 처음 부터 자료를 저장  2. 빈배열  3. 빈 배열을 만들고 한 개씩 추가

# season = "여름"  # 변수
seasons = ["봄","여름","가을","겨울"]

# print(season)
print(seasons[0])
print(seasons[1])
print(seasons[2])
print(seasons[3])
print(seasons[-1])  # 맨 끝 요소에 접근(셀 수 있는 정도가 아닌 셀 수 없이 많을 때 사용)
print(seasons)


animals = [ ]  # 동물을 담을 빈 리스트 생성
animals.append("강아지")  # append()를 사용해 리스트에 강아지가 추가함
animals.append("고양이")

print(animals) # 출력하면 리스트에 저장되어 있는 값들이 출력됨 -> ['강아지','고양이']
print(type(animals)) # type()을 이용해 animal의 상태를 출력할 수 있음 -> <class 'list'>

