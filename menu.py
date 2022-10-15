import complexn as c
import ration as r
import log as l
from init_status import status_prog
import out as o


def menu():
    print((
        'Вас приветствует калькулятор!\n'
        'Для работы с рациональными или комплексными числами выберите режим:\n'
        'Введите 1 или 2.\n'
        '1. Рациональные.\n'
        '2. Комплексные.\n'
        'Для доступа к логам, введите "log"\n'
        '------------------'
    ))


def mn_select(cl):
    status = False
    while status != True:
        if cl == '1':
            status = True
            o.out_result(r.ration())

        elif cl == '2':
            status = True
            o.out_result(c.complex_new())
        elif cl == 'log':
            l.view_log()
            status = True
        else:
            print(('Неккоректный ввод! Введите 1 или 2!\n'
                   '----------------------------------'))
            cl = input()
            l.loging(f'Ввод пользователем {cl}')


def stop_prog():
    print(('Вы хотите продолжить работу с калькулятором?\n'
           'Для продолжения нажмите enter\n'
           'Для выхода введите "n"\n'))
    n = input('>> ')
    if n == 'n':
        return False
