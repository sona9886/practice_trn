# 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자.
# 즉 다음과 같이 동작해야 한다.
# cal = MaxLimitCalculator()
# cal.add(50) # 50 더하기
# cal.add(60) # 60 더하기
# print(cal.value) # 100 출력
# 단, 반드시 다음과 같은 Calculator 클래스를 상속해서 만들어야 한다.

class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val): #. 메서드 오버라이딩: 동일한 함수에 내용 덮어쓰기
        self.value += val
        if self.value > 100:
            self.value = 100    #. return을 쓰고싶으면, return self.value 하면 됨
                    
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)