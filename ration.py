from fractions import Fraction
import log as l
import calculation as c
import vvod as v


def ration():
    v.vvod()
    print('Вычисление рациональных чисел.')
    a = Fraction(v.a)
    operation = v.operation
    b = Fraction(v.b)
    c.calc(a, b, operation)
    answer = c.answer
    l.loging(f'первое число - {a}, второе - {b}, операция - {operation}, результат - {answer} ')
    return answer
