import math
  import time
def myDecorator(myFunction):
        print('Вызвана функция: {}'.format(myFunction.__name__))
        myFunction() 
        print('затраченное время: %s' % time.perf_counter())   
def ():
    print('Введите длину и ширину:')
    lenght = int(input())
    width = int(input())
    temporary = lenght * width
    SQFT_PER_ACRE = temporary / 43560
    print("Результат =", SQFT_PER_ACRE, "акров")

 deffreeFall(accseleration = 9,8):
    print('Введите дистанцию:')
    distance = int(input())
    Vf = math.sqrt(2 * (  accseleration*distance))
    print('Скорость объекта при его соприкосновении с землей: ', Vf)
    
myDecorator(areaCalculation)
myDecorator(freeFall)
