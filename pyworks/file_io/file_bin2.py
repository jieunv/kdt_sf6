# 이미지 파일 읽고 쓰기
with open('simba.jpg', 'rb') as f1:
    img = f1.read()

with open('./output/simba.jpg', 'wb') as f2:
    f2.write(img)

