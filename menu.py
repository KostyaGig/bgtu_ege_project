from print_utils import *
from select_task_data import *

TYPE_OF_TASK_KEY = "type_of_task"
PASSWORD_LENGTH_KEY = "password_length"
PASSWORD_SYMBOLS_KEY = "password_symbols"
COUNT_OF_PASSWORDS_KEY = "count_of_passwords"
EXTRA_INFO_KEY = "extra_info"

EXIT_MENU_ITEM_NUMBER = "0"
TYPE_OF_TASK_MENU_ITEM_NUMBER = "1"

CONFIGURE_PASSWORD_MENU_ITEM_NUMBER = "2"
ENTER_LENGTH_OF_PASSWORD_MENU_SUB_ITEM_NUMBER = "2.1"
ENTER_SYMBOLS_OF_PASSWORD_MENU_SUB_ITEM_NUMBER = "2.2"
ENTER_COUNT_OF_PASSWORDS_MENU_SUB_ITEM_NUMBER = "2.3"
ENTER_INFO_MENU_SUB_ITEM_NUMBER = "2.4"

menu_dict = {
    TYPE_OF_TASK_MENU_ITEM_NUMBER: "choose what type of task to generate",
    CONFIGURE_PASSWORD_MENU_ITEM_NUMBER: "configure password",
    ENTER_LENGTH_OF_PASSWORD_MENU_SUB_ITEM_NUMBER: "enter password's length",
    ENTER_SYMBOLS_OF_PASSWORD_MENU_SUB_ITEM_NUMBER: "enter password's symbols",
    ENTER_COUNT_OF_PASSWORDS_MENU_SUB_ITEM_NUMBER: "enter count of passwords",
    ENTER_INFO_MENU_SUB_ITEM_NUMBER: "enter extra info",
}

menu_path = []

def print_menu_path():
    print("Path:", end=' ')
    last_item = menu_path[-1]
    for item in menu_path:
        separator = "->" if item != last_item else ""
        print(item, separator, end=' ')

def update_menu_path_if_need(item):
    if item in menu_dict:
        menu_path.append(menu_dict[item])
        print_menu_path()


def call_configure_password_menu(task_configuration, is_recursive=True):
    if is_recursive:
        menu_path.pop()
        print_menu_path()

    add_space()
    print("1 - Enter length of password")
    print("2 - Enter symbols of password")
    print("3 - Enter count of passwords")
    print("4 - Enter extra info")
    print("0 - Back")

    item = str(input("item: "))

    while not item.isnumeric() or not (-1 < int(item) < 5):
        item = str(input("select corrected menu item: "))

    update_menu_path_if_need(CONFIGURE_PASSWORD_MENU_ITEM_NUMBER + "." + item)
    item_as_int = int(item)

    if item_as_int == 1:
        task_configuration[PASSWORD_LENGTH_KEY] = select_and_return_type_password_length()
    elif item_as_int == 2:
        task_configuration[PASSWORD_SYMBOLS_KEY] = select_and_return_password_symbols()
    elif item_as_int == 3:
        task_configuration[COUNT_OF_PASSWORDS_KEY] = select_and_return_count_of_passwords()
    elif item_as_int == 4:
        task_configuration[EXTRA_INFO_KEY] = select_and_return_extra_info()

    if 1 <= item_as_int <= 4: call_configure_password_menu(task_configuration, is_recursive=True)


def call_start_menu(task_configuration, is_not_first_call=True):
    while len(menu_path) != 1:
        menu_path.pop()
    if is_not_first_call: print_menu_path()

    print("\n1 - Choose what type of task to generate")
    print("2 - Configure password ")
    print("0 - Exit ")

    item = str(input("item: "))
    while not item.isnumeric() or not (-1 < int(item) < 3):
        item = str(input("select corrected menu item: "))

    if item == EXIT_MENU_ITEM_NUMBER:
        return

    update_menu_path_if_need(item)
    if item == TYPE_OF_TASK_MENU_ITEM_NUMBER:
        add_space()
        print("1 - Пароли")
        print("2 - Пароли с дополнительными сведениями")
        print("3 - Случайным образом")
        print("0 - Back")

        item = str(input("item: "))
        while not item.isnumeric() or not (-1 < int(item) < 4):
            item = str(input("select corrected menu item: "))
        if int(item) != 0:
            task_configuration[TYPE_OF_TASK_KEY] = int(item)
        call_start_menu(task_configuration)
    else:
        call_configure_password_menu(task_configuration, is_recursive=False)
        call_start_menu(task_configuration)

def configure_task_using_menu(task_configuration):
    print_with_space("--------Menu--------")
    menu_path.append("menu")
    print_menu_path()
    add_space()

    call_start_menu(task_configuration, is_not_first_call=False)
