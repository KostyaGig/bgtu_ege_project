import random

TYPE_OF_TASK_MIN = 1
TYPE_OF_TASK_MAX = 2

PASSWORD_LENGTH_MIN = 1
PASSWORD_LENGTH_MAX = 100

COUNT_PASSWORDS_MIN = 1
COUNT_PASSWORDS_MAX = 2 ** 12

EXTRA_INFO_IN_BYTES_MIN = 3
EXTRA_INFO_IN_BYTES_MAX = 33

COUNT_OF_RANDOM_SYMBOLS_MIN = 1
COUNT_OF_RANDOM_SYMBOLS_MAX = 111

RANDOM_ASCII_SYMBOL_MIN = 30
RANDOM_ASCII_SYMBOL_MAX = 122


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

    while count_of_unique_symbols != 0:
        random_ascii_symbol_in_range = random.randrange(RANDOM_ASCII_SYMBOL_MIN, RANDOM_ASCII_SYMBOL_MAX + 1)
        password_symbols.add(chr(random_ascii_symbol_in_range))
        count_of_unique_symbols = count_of_unique_symbols - 1
    return password_symbols
