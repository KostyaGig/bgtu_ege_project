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
