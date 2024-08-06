input_num = input("숫자 입력: ").split(" ") #문자가 저장됨
numbers = [] #숫자를 저장할 리스트
for i in input_num:
    numbers.append(int(i))
print(numbers)

max_val = max(numbers)
print(f'가장 큰 값: {max_val}')
min_val = min(numbers)
print(f'가장 작은 값: {min_val}')

numbers.remove(max_val)
numbers.remove(min_val)

# sum()
print(f'나머지 값의 평균: {int(sum(numbers) / len(numbers))}')