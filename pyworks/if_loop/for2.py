# for in 리스트

shop = ['반팔', '바지', '이어폰', '키보드']

print('바지' in shop) #True
print('양말' in shop) #False
print('양말' not in shop) #True

#마우스 추가하기 - append()는 요소를 하나만 추가할 때
shop.append("마우스")
print(shop[:])

#리스트에 요소 2개 이상 추가하기
shop.extend(['커피', '비스켓'])
print(shop[:])

for i in shop:
    print(i)

#이어폰 삭제
shop.remove("이어폰")
print(shop[:])
for i in shop:
    print(i, end=" ")

# 리스트의 연산
# 개수(len), 합계(sum/total+i),평균, 최대값, 최소값
score = [70, 80, 60, 90, 40]
print(f'개수: {len(score)}')
print(f'합계: {sum(score)}')
print(f'평균: {sum(score) / len(score)}')
print(f'최대값: {max(score)}')
print(f'최소값: {min(score)}')

#합계
sum_v = 0 #초기화
for i in score:
    sum_v += i
print(f'합계: {sum_v}')
print(f'최대값: {max(score)}')
max_v = score[0] #처음값으로 초기화
n = len(score)
for i in range(0, n): #n+1이 아닌 n
    if score[i] > max_v: #
        max_v = score[i]

'''#최대값
i = 1, 80 > 70, max_v = 80
i = 2, 60 > 80, max_v = 80
i = 3, 90 > 80, max_v = 90
i = 3, 40 > 90, max_v = 90
'''

max_v = -99 # 매우 작은값으로 초기화
for i in score: # i-리스트의 요소
    if i > max_v:
        max_v = i

print(f'최대값: {max_v}')