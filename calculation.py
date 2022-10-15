answer = 0


def calc(a, b, operation):
    global answer
    if operation == '+':
        answer = a + b
    elif operation == '-':
        answer = a - b
    elif operation == '*':
        answer = a * b
    elif operation == '/':
        answer = a / b
    else:
        print('Введите верные значения!')
    return answer
