# 별찍기

# 직각 삼각형
for i in range(1,5):
    print("*" * i)

print("="*20) # 구분선

# 공백이 먼저인 직각 삼각형
for i in range(1,5):
    print(" " * (4-i) + "*" * i)

print("="*20) # 구분선

# 정삼각형
for i in range(1,6):
    print(" " * (5 - i) + "*" * (i * 2 - 1))