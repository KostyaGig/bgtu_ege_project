import time

import select_task_data
from solve_tasks import *
from random_task_data_generator import *
from print_utils import add_space
from task_data_printer import print_task_to_file, print_task_condition_and_answer_to_console_with_task_number

PASSWORD_TYPE_OF_TASK = 1
PASSWORD_WITH_EXTRA_DATA_TYPE_OF_TASK = 2
RANDOM_TYPE_OF_TASK = 3

FIRST_TYPE_OF_TASK_FILE_TEMPLATE_PATH = "task_templates/password/1.txt"
SECOND_TYPE_OF_TASK_FILE_TEMPLATE_PATH = "task_templates/password_with_extra_information/1.txt"
OUTPUT_FILE_PATH = "output.txt"

TASK_GENERATING_DELAY_IN_SECONDS = 0.7


def generate_first_type_of_task(password_length, password_symbols, count_of_passwords):
    try:
        with open(FIRST_TYPE_OF_TASK_FILE_TEMPLATE_PATH, "r") as file:
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


def generate_second_type_of_task(password_length, password_symbols, count_of_passwords, extra_info):
    try:
        with open(SECOND_TYPE_OF_TASK_FILE_TEMPLATE_PATH, "r") as file:
            task_condition_as_string = file.read()
            task_condition_as_string = task_condition_as_string \
                .replace("15", str(password_length)) \
                .replace("12", str(len(password_symbols))) \
                .replace("А, В, C, D, Е, F, G, H, К, L, M, N", str(password_symbols)) \
                .replace("{", "") \
                .replace("}", "") \
                .replace("14", str(extra_info)) \
                .replace("50", str(count_of_passwords))
            return task_condition_as_string
    except Exception as error:
        print(f"During generating second type of task {error} error occured...")
    finally:
        file.close()


def randomly_generate_tasks():
    countOfTasks = select_task_data.select_count_of_tasks()
    try:
        with open(OUTPUT_FILE_PATH, "w") as file:
            for index in range(0, int(countOfTasks)):
                add_space()

                print(f"Generating condition for {index + 1} task...")
                time.sleep(TASK_GENERATING_DELAY_IN_SECONDS)

                password_length = generate_random_password_length()
                count_of_passwords = generate_count_of_passwords()
                password_symbols = generate_random_set_of_symbols()
                random_type_of_task = generate_random_type_of_task()

                if random_type_of_task == PASSWORD_TYPE_OF_TASK:
                    condition = generate_first_type_of_task(password_length, password_symbols, count_of_passwords)
                    answer = solve_first_type_of_task(password_length, password_symbols, count_of_passwords)
                else:
                    extra_info_in_bytes = generate_random_extra_info_in_bytes()
                    condition = generate_second_type_of_task(password_length, password_symbols, count_of_passwords,
                                                             extra_info_in_bytes)
                    answer = solve_second_type_of_task(password_length, password_symbols, count_of_passwords,
                                                       extra_info_in_bytes)

                print_task_condition_and_answer_to_console_with_task_number(condition, answer, index)
                print_task_to_file(condition, answer, file, index)

    except Exception as error:
        print(f"During randomly generate task {index + 1}  {error} error occured...")
    finally:
        file.close()


def generate_condition_and_answer_in_depending_on_type_of_task(
        type_of_task,
        password_length,
        password_symbols,
        count_of_passwords,
        extra_info
):
    if type_of_task == PASSWORD_TYPE_OF_TASK:
        extra_info = 0
        condition = generate_first_type_of_task(password_length, password_symbols, count_of_passwords)
        answer = solve_first_type_of_task(password_length, password_symbols, count_of_passwords)
    else:
        condition = generate_second_type_of_task(password_length, password_symbols, count_of_passwords, extra_info)
        answer = solve_second_type_of_task(password_length, password_symbols, count_of_passwords, extra_info)

    return condition, answer
