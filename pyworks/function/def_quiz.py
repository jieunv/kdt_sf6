'''def same(x,y):
    if x == y:
        return x*y
    else:
        return x+y
print(f'결과(곱): {same(x=2, y=2)}')
print(f'결과(합): {same(x=2, y=3)}')
'''
def get_price(x,y):
    if x*y < 20000:
        return (x*y)+2500
    else:
        return x*y

print(f'상품1 가격: {get_price(10000, 3)}원')
print(f'상품2 가격: {get_price(5000,3)}원')