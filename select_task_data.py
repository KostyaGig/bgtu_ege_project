from random_task_data_generator import generate_random_type_of_task
from task_generator import PASSWORD_WITH_EXTRA_DATA_TYPE_OF_TASK

TASK_CONFIG_NO_VALUE = "-1"


def select_and_return_type_password_length_if_need(password_length):
    if password_length == TASK_CONFIG_NO_VALUE:
        password_length = select_and_return_type_password_length()
    return password_length

def select_and_return_type_password_length():
    print("\nEnter length of password: ")
    length = str(input("length: "))

    while not length.isnumeric() or (int(length) < 1):
        length = str(input("enter corrected length of password in range(1, inf): "))
    return int(length)


def select_and_return_count_of_passwords_if_need(count_of_passwords):
    if count_of_passwords == TASK_CONFIG_NO_VALUE:
        count_of_passwords = select_and_return_count_of_passwords()
    return count_of_passwords

def select_and_return_count_of_passwords():
    print("\nEnter count of passwords: ")
    count = input("count: ")

    while not count.isnumeric() or (int(count) < 1):
        count = input("enter corrected count in range(1, inf): ")
    return int(count)

def select_and_return_password_symbols_if_need(password_symbols):
    if password_symbols == TASK_CONFIG_NO_VALUE:
        password_symbols = select_and_return_password_symbols()
    return password_symbols

def select_and_return_password_symbols():
    print("\nEnter symbols of password: ")
    symbols = str(input("symbols: "))

    while not symbols:
        symbols = str(input("enter at least 1 symbol: "))
    return set(symbols)

def select_and_return_extra_info_if_need(type_of_task, extra_info):
    if type_of_task == PASSWORD_WITH_EXTRA_DATA_TYPE_OF_TASK and extra_info == TASK_CONFIG_NO_VALUE:
        extra_info = select_and_return_extra_info()
    return extra_info

def select_and_return_extra_info():
    print("\nEnter extra info in bytes: ")
    extra_info_in_bytes = input("extra_info_in_bytes: ")
    while not extra_info_in_bytes.isnumeric() or int(extra_info_in_bytes) < 1:
        extra_info_in_bytes = input("extra_info_in_bytes(1, inf): ")
    return int(extra_info_in_bytes)

def select_and_return_type_of_task():
    print("Select type of task: ")
    print("1 - Пароли")
    print("2 - Пароли с дополнительными сведениями")
    print("3 - Случайным образом")

    item = str(input("item: "))
    while not item.isnumeric() or not (-1 < int(item) < 4):
        item = str(input("select corrected menu item: "))
    if item == 3: item = generate_random_type_of_task()
    return int(item)


def select_count_of_tasks():
    print("\nEnter count of tasks: ")
    countOfTasks = input("count: ")
    while not countOfTasks.isnumeric() or int(countOfTasks) < 1:
        countOfTasks = input("enter corrected count of tasks to generate randomly: ")
    return countOfTasks
