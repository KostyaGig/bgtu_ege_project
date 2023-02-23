import random
import time

from menu import *

TYPE_OF_TASK_MIN = 1
TYPE_OF_TASK_MAX = 2

PASSWORD_LENGTH_MIN = 1
PASSWORD_LENGTH_MAX = 100

COUNT_PASSWORDS_MIN = 1
COUNT_PASSWORDS_MAX = 2 ** 12

EXTRA_INFO_IN_BYTES_MIN = 3
EXTRA_INFO_IN_BYTES_MAX = 33

TASK_CONFIG_NO_VALUE = "-1"

PASSWORD_TYPE_OF_TASK = 1
PASSWORD_WITH_EXTRA_DATA_TYPE_OF_TASK = 2
RANDOM_TYPE_OF_TASK = 3

TASK_GENERATING_DELAY_IN_SECONDS = 0.7

# todo add extra bytes key
task_configuration = {
    TYPE_OF_TASK_KEY: TASK_CONFIG_NO_VALUE,
    PASSWORD_LENGTH_KEY: TASK_CONFIG_NO_VALUE,
    PASSWORD_SYMBOLS_KEY: TASK_CONFIG_NO_VALUE,
    COUNT_OF_PASSWORDS_KEY: TASK_CONFIG_NO_VALUE,
    EXTRA_INFO_KEY: TASK_CONFIG_NO_VALUE,
}

COUNT_OF_RANDOM_SYMBOLS_MIN = 1
COUNT_OF_RANDOM_SYMBOLS_MAX = 111

RANDOM_ASCII_SYMBOL_MIN = 30
RANDOM_ASCII_SYMBOL_MAX = 122

type_of_task_dict = {
    1: "Пароли",
    2: "Пароли с дополнительными сведениями"
}

MENU_MENU_ITEM = 1
START_MENU_ITEM = 2
RANDOM_MENU_ITEM = 3


# todo move to shared method to reuse this code in menu.py
def select_and_return_menu_item():
    print("1 - Menu")
    print("2 - Start")
    print("3 - Random generation N tasks to output file")
    item = str(input("item: "))
    while not item.isnumeric() or not (0 < int(item) < 4):
        item = str(input("select corrected menu item: "))
    return int(item)


# todo move to shared method to reuse this code in menu.py
def select_and_return_type_password_length():
    print("\nEnter length of password: ")
    length = str(input("length: "))

    while not length.isnumeric() or (int(length) < 1):
        length = str(input("enter corrected length of password in range(1, inf): "))
    return int(length)


# todo move to shared method to reuse this code in menu.py
def select_and_return_count_of_passwords():
    print("\nEnter count of passwords: ")
    count = input("count: ")

    while not count.isnumeric() or (int(count) < 1):
        count = input("enter corrected count in range(1, inf): ")
    return int(count)


# todo move to shared method to reuse this code in menu.py
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


# todo move to shared method to reuse this code in menu.py
def select_and_return_password_symbols():
    print("\nEnter symbols of password: ")
    symbols = str(input("symbols: "))

    while not symbols:
        symbols = str(input("enter at least 1 symbol: "))
    return set(symbols)


# todo move to shared method to reuse this code in menu.py
def select_and_return_extra_info():
    print("\nEnter extra info in bytes: ")
    extra_info_in_bytes = input("extra_info_in_bytes: ")
    while not extra_info_in_bytes.isnumeric() or int(extra_info_in_bytes) < 1:
        extra_info_in_bytes = input("extra_info_in_bytes(1, inf): ")
    return int(extra_info_in_bytes)


# todo move to separate file
def generate_random_type_of_task():
    return random.randrange(TYPE_OF_TASK_MIN, TYPE_OF_TASK_MAX + 1)


def generate_random_password_length():
    return random.randrange(PASSWORD_LENGTH_MIN, PASSWORD_LENGTH_MAX + 1)


def generate_count_of_passwords():
    return random.randrange(COUNT_PASSWORDS_MIN, COUNT_PASSWORDS_MAX + 1)


def generate_random_extra_info_in_bytes():
    return random.randrange(EXTRA_INFO_IN_BYTES_MIN, EXTRA_INFO_IN_BYTES_MAX + 1)


def generate_cyrillic_set_of_symbols():
    password_symbols = set()
    a = ord('а')
    for i in range(a, a + 32):
        password_symbols.add(chr(i))
    return password_symbols


def generate_random_set_of_symbols():
    password_symbols = set()
    count_of_unique_symbols = random.randrange(COUNT_OF_RANDOM_SYMBOLS_MIN, COUNT_OF_RANDOM_SYMBOLS_MAX + 1)

    while (count_of_unique_symbols != 0):
        random_ascii_symbol_in_range = random.randrange(RANDOM_ASCII_SYMBOL_MIN, RANDOM_ASCII_SYMBOL_MAX + 1)
        password_symbols.add(chr(random_ascii_symbol_in_range))
        count_of_unique_symbols = count_of_unique_symbols - 1
    return password_symbols


def build_task():
    type_of_task = task_configuration[TYPE_OF_TASK_KEY]
    password_length = task_configuration[PASSWORD_LENGTH_KEY]
    password_symbols = task_configuration[PASSWORD_SYMBOLS_KEY]
    count_of_passwords = task_configuration[COUNT_OF_PASSWORDS_KEY]
    extra_info = task_configuration[EXTRA_INFO_KEY]

    if type_of_task == TASK_CONFIG_NO_VALUE:
        type_of_task = select_and_return_type_of_task()

    if type_of_task == 3:
        type_of_task = generate_random_type_of_task()

    if password_length == TASK_CONFIG_NO_VALUE:
        password_length = select_and_return_type_password_length()
    if count_of_passwords == TASK_CONFIG_NO_VALUE:
        count_of_passwords = select_and_return_count_of_passwords()
    if password_symbols == TASK_CONFIG_NO_VALUE:
        password_symbols = select_and_return_password_symbols()
    if extra_info == TASK_CONFIG_NO_VALUE:
        if type_of_task == 2:
            extra_info = select_and_return_extra_info()

    if type_of_task == 1:
        extra_info = 0
        condition = generate_first_type_of_task(password_length, password_symbols, count_of_passwords)
        answer = solve_first_type_of_task(password_length, password_symbols, count_of_passwords)
    else:
        condition = generate_second_type_of_task(password_length, password_symbols, count_of_passwords, extra_info)
        answer = solve_second_type_of_task(password_length, password_symbols, count_of_passwords, extra_info)

    print("\n --------- Metadata ---------")
    print("Type of task: ", type_of_task_dict[type_of_task])
    print("Password's length: ", password_length)
    print("Password's symbols: ", password_symbols)
    print("Count of passwords: ", count_of_passwords)
    if extra_info != 0: print("Extra info in bytes: ", extra_info)

    print("\n --------- Task ---------")
    print(condition)
    print(f"Answer: {str(answer)} Байт")


def randomly_generate_tasks():
    countOfTasks = input("count: ")
    while not countOfTasks.isnumeric() or int(countOfTasks) < 1:
        countOfTasks = input("enter corrected count of tasks to generate randomly: ")

    try:
        with open('output.txt', 'w') as file:
            for index in range(0, int(countOfTasks)):
                add_space()
                print(f"Generating condition for {index + 1} task...")

                password_length = generate_random_password_length()
                count_of_passwords = generate_count_of_passwords()

                time.sleep(TASK_GENERATING_DELAY_IN_SECONDS)
                print("generating symbols...")
                add_space()
                password_symbols = generate_random_set_of_symbols()

                random_type_of_task = generate_random_type_of_task()
                print(random_type_of_task)
                if random_type_of_task == 1:
                    condition = generate_first_type_of_task(password_length, password_symbols, count_of_passwords)
                    answer = solve_first_type_of_task(password_length, password_symbols, count_of_passwords)
                else:
                    extra_info_in_bytes = generate_random_extra_info_in_bytes()
                    condition = generate_second_type_of_task(password_length, password_symbols, count_of_passwords,
                                                             extra_info_in_bytes)
                    answer = solve_second_type_of_task(password_length, password_symbols, count_of_passwords,
                                                       extra_info_in_bytes)

                print(condition)
                # print(answer)
                file.write(f"-------------------- Task {index + 1} --------------------")
                file.write("\n")
                file.write(condition)
                file.write("\n")
                file.write("Answer: ")
                file.write(str(answer))
                file.write(" Байт")
                file.write("\n\n\n")
    except Exception as error:
        print(f"During randomly generate task {index + 1}  {error} error occured...")
    finally:
        file.close()


def find_count_of_bits_for_one_symbol_for_length(password_length):
    power = 1
    curr = 2
    while password_length > curr:
        power = power + 1
        curr = 2 ** power
    return power


def min_count_of_bytes(bits):
    (div, mod) = divmod(bits, 8)
    return div + 1 if (mod != 0) else div


def solve(password_length, password_symbols_length, count_of_passwords, extra_info_in_bytes):
    count_of_bits_for_one_symbol = find_count_of_bits_for_one_symbol_for_length(password_symbols_length)
    bits_need_for_one_password = count_of_bits_for_one_symbol * password_length
    count_of_bytes_for_one_password = min_count_of_bytes(bits_need_for_one_password)

    return (count_of_bytes_for_one_password + extra_info_in_bytes) * count_of_passwords


def solve_first_type_of_task(password_length, password_symbols, count_of_passwords):
    return solve(password_length, len(password_symbols), count_of_passwords, 0)


def solve_second_type_of_task(password_length, password_symbols, count_of_passwords, extra_info_in_bytes):
    return solve(password_length, len(password_symbols), count_of_passwords, extra_info_in_bytes)


def generate_first_type_of_task(password_length, password_symbols, count_of_passwords):
    try:
        with open('task_templates/password/1.txt', 'r') as file:
            task_condition_as_string = file.read()
            task_condition_as_string = task_condition_as_string \
                .replace("9", str(password_length)) \
                .replace("A, B, C, D, E, F", str(password_symbols)) \
                .replace("{", "") \
                .replace("}", "") \
                .replace("50", str(count_of_passwords))
            return task_condition_as_string
    except Exception as error:
        print(f"During generating first type of task {error} error occured...")
    finally:
        file.close()


def generate_second_type_of_task(password_length, password_symbols, count_of_passwords, extra_info_in_bytes):
    try:
        with open('task_templates/password_with_extra_information/1.txt', 'r') as file:
            task_condition_as_string = file.read()
            task_condition_as_string = task_condition_as_string \
                .replace("15", str(password_length)) \
                .replace("12", str(len(password_symbols))) \
                .replace("А, В, C, D, Е, F, G, H, К, L, M, N", str(password_symbols)) \
                .replace("{", "") \
                .replace("}", "") \
                .replace("14", str(extra_info_in_bytes)) \
                .replace("50", str(count_of_passwords))
            return task_condition_as_string
    except Exception as error:
        print(f"During generating second type of task {error} error occured...")
    finally:
        file.close()


if __name__ == '__main__':
    item = select_and_return_menu_item()
    if item == MENU_MENU_ITEM:
        configure_task_using_menu(task_configuration)
        build_task()
    elif item == RANDOM_MENU_ITEM:
        randomly_generate_tasks()
    else:
        build_task()
