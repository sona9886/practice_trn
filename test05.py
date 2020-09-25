# 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
# >>> hex(234)
# '0xea'
# 이번에는 반대로 16진수 문자열 0xea를 10진수로 변경해 보자.
# ※ 내장 함수 int를 활용해 보자.

print(hex(234))
print(int(0xea))

#. 입력받은 수를 16진수로 > 10진수로 변환하는 함수
class Sixteen:
    def __init__(self):
        self.value = 0
    def sixteen(self):
        value = int(input('10진수 수를 입력하세요: '))
        ten = value
        global sixteen
        sixteen = hex(ten)
        print('입력하신 {}를 16진수로 변환한 값은 {}입니다.'.format(ten, sixteen))  

class Ten(Sixteen):
    def ten(self):
        ten = int(sixteen, 16)
        print('16진수인 {}를 10진수로 변환한 값은 {}입니다.'.format(sixteen, ten))

change = Ten()
change.sixteen()
change.ten()