import re
from email.quoprimime import body_length


def get_reg_data():
    match_name = re.compile(r"^[a-zA-Zа-яА-Я]+$")
    match_surname = re.compile(r"^[a-zA-Zа-яА-Я]+$")
    match_phone = re.compile(r"^(\+\d{3})(\(\d{2}\))(\d{7})$")
    match_email = re.compile(r"^[a-zA-Z_0-9]+@yandex\.ru$")

    reg_lists = [match_name, match_surname, match_phone, match_email]
    return reg_lists

