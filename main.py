from menu import *
from select_task_data import *
from task_generator import *
from task_data_printer import print_task_metadata_to_console, print_task_condition_and_answer_to_console

task_configuration = {
    TYPE_OF_TASK_KEY: TASK_CONFIG_NO_VALUE,
    PASSWORD_LENGTH_KEY: TASK_CONFIG_NO_VALUE,
    PASSWORD_SYMBOLS_KEY: TASK_CONFIG_NO_VALUE,
    COUNT_OF_PASSWORDS_KEY: TASK_CONFIG_NO_VALUE,
    EXTRA_INFO_KEY: TASK_CONFIG_NO_VALUE,
}

type_of_task_dict = {
    1: "Пароли",
    2: "Пароли с дополнительными сведениями"
}

MENU_MENU_ITEM = 1
START_MENU_ITEM = 2
RANDOM_MENU_ITEM = 3


def select_and_return_menu_item():
    print("1 - Menu")
    print("2 - Start")
    print("3 - Random generation N tasks to output file")
    item = str(input("item: "))

    while not item.isnumeric() or not (0 < int(item) < 4):
        item = str(input("select corrected menu item: "))
    return int(item)


def build_task():
    type_of_task = task_configuration[TYPE_OF_TASK_KEY]
    password_length = task_configuration[PASSWORD_LENGTH_KEY]
    password_symbols = task_configuration[PASSWORD_SYMBOLS_KEY]
    count_of_passwords = task_configuration[COUNT_OF_PASSWORDS_KEY]
    extra_info = task_configuration[EXTRA_INFO_KEY]

    if type_of_task == TASK_CONFIG_NO_VALUE:
        type_of_task = select_and_return_type_of_task()

    if type_of_task == RANDOM_TYPE_OF_TASK:
        type_of_task = generate_random_type_of_task()

    password_length = select_and_return_type_password_length_if_need(password_length)
    count_of_passwords = select_and_return_count_of_passwords_if_need(count_of_passwords)
    password_symbols = select_and_return_password_symbols_if_need(password_symbols)
    extra_info = select_and_return_extra_info_if_need(type_of_task, extra_info)

    condition, answer = generate_condition_and_answer_in_depending_on_type_of_task(
        type_of_task,
        password_length,
        password_symbols,
        count_of_passwords,
        extra_info
    )

    print_task_metadata_to_console(
            type_of_task_dict[type_of_task],
            password_length,
            password_symbols,
            count_of_passwords,
            extra_info
        )

    print_task_condition_and_answer_to_console(condition, answer)


if __name__ == '__main__':
    item = select_and_return_menu_item()
    if item == MENU_MENU_ITEM:
        configure_task_using_menu(task_configuration)
        build_task()
    elif item == RANDOM_MENU_ITEM:
        randomly_generate_tasks()
    else:
        build_task()
