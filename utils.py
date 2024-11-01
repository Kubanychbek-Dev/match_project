import re


def get_reg_data():
    match_name = re.compile(r"^[a-zA-Zа-яА-Я]+$")
    match_surname = re.compile(r"^[a-zA-Zа-яА-Я]+$")
    match_phone = re.compile(r"^(\+\d{3})(\(\d{2}\))(\d{7})$")
    match_email = re.compile(r"^[a-zA-Z_0-9]+@yandex\.ru$")

    reg_lists = [match_name, match_surname, match_phone, match_email]
    return reg_lists


def reg_check(user_data, users_list):
    regex = get_reg_data()
    for i in regex:
        if bool(i.fullmatch(user_data)) is True:
            if user_data not in users_list:
                return user_data


def check_unique_data(user_data, data_to_check):
    if user_data not in data_to_check:
        data_to_check.append(user_data)
    else:
        print("Уже есть пользователь с точно такими же данными, введите другие данные")
        print()