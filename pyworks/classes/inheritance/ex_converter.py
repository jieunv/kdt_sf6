# 단위 변환기 확장 클래스
# 클래스의 상속 기능 구현
# F(화씨) = C(섭씨) * 1.8 + 32

from classes.class_scale_converter import ScaleConverter #파일 안에 있는 클래스 임포트

class Converter(ScaleConverter): # 상속 클래스가 괄호 안에 들어가면 된다
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor) #부모 클래스의 멤버를 모두 적어줌
        self.offset = offset # 자기 멤버

    # 메서드 재정의
    def convert(self, value):
        return value * self.factor + self.offset

    def __str__(self):
        return f'{self.units_from} {self.units_to} {self.factor} {self.offset}'

conv = Converter("C", 'F', 1.8, 32)
# print(conv)
print(f'33{conv.units_from} = {conv.convert(33)}{conv.units_to}')
