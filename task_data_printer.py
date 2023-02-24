def print_task_to_file(condition, answer, file, index):
    file.write(f"-------------------- Task {index + 1} --------------------")
    file.write("\n")
    file.write(condition)
    file.write("\n")
    file.write("Answer: ")
    file.write(str(answer))
    file.write(" Байт")
    file.write("\n\n\n")

def print_task_metadata_to_console(type_of_task, password_length, password_symbols, count_of_passwords, extra_info):
    print("\n --------- Metadata ---------")
    print("Type of task: ", type_of_task)
    print("Password's length: ", password_length)
    print("Password's symbols: ", password_symbols)
    print("Count of passwords: ", count_of_passwords)
    if extra_info != 0: print("Extra info in bytes: ", extra_info)

def print_task_condition_and_answer_to_console(condition, answer):
    print("\n --------- Task ---------")
    print(condition)
    print(f"Answer: {str(answer)} Байт")

def print_task_condition_and_answer_to_console_with_task_number(condition, answer, index):
    print(f"\n --------- Task {index + 1} ---------")
    print(condition)
    print(f"Answer: {str(answer)} Байт")