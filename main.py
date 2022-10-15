import menu
import select as s

import log as l
from init_status import status_prog


while status_prog != False:
    menu.menu()
    s.click()
    l.loging(f'Ввод пользователем {s.text_from_user}')
    menu.mn_select(s.text_from_user)
    status_prog = menu.stop_prog()

    
