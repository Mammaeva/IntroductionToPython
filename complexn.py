import log as l
import vvod as v
import calculation as c


def complex_new():
    v.vvod()
    print('Вычисление комплексных чисел.')
    a = complex(v.a)
    operation = v.operation
    b = complex(v.b)
    c.calc(a, b, operation)
    answer = c.answer
    l.loging(f'первое число - {a}, второе - {b}, операция - {operation}, результат - {answer} ')
    return answer
