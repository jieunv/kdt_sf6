# 리스트 함수

# 추가 - 리스트.append()
# 삭제 - 리스트.pop(), 리스트.remove()
# 정렬 - 리스트.sort() , 뒤집기 - reverse()

lower = ['b','d','a','c']
# 정렬(오름차순)
# 'e' 추가
lower.sort()
print(lower)

lower.reverse()
print(lower)

'''
lower.append('e') # append() 함수는 추가는 되지만 맨 뒤에 추가가 됨
print(lower)

# 'e'삭제
lower.pop() # 맨 뒤 삭제
print(lower)

# 'b'와 'c' 사이에 'e' 추가
lower.insert(__index=2,__object='e')
print(lower)

# 'c' 삭제
lower.remove('c')
print(lower)
'''