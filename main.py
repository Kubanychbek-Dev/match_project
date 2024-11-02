from utils import reg_check, check_unique_data

users_list = []

while len(users_list) < 3:
    user_data_list = []

    ask_name_i = 0

    while ask_name_i < 1:
        ask_name = input("Введите имя пользователя: ").strip().title()
        result = reg_check(ask_name, user_data_list)
        if result:
            print("Имя принято")
            print()
            ask_name_i += 1
        else:
            print("Содержит неподходящие символы")
            print()


    ask_surname_i = 0

    while ask_surname_i < 1:
        ask_surname = input("Введите фамилию пользователя: ").strip().title()
        result = reg_check(ask_surname, user_data_list)
        if result:
            print("Фамиля принята")
            print()
            ask_surname_i += 1
        else:
            print("Содержит неподходящие символы")
            print()

    ask_phone_i = 0

    while ask_phone_i < 1:
        ask_phone_number = input("Введите телефон в формате +***(**)*******: ").strip()
        result = reg_check(ask_phone_number, user_data_list)
        if result:
            print("Телефон принят")
            print()
            ask_phone_i += 1
        else:
            print("Не соответствует формату +***(**)*******")
            print()

    ask_email_i = 0

    while ask_email_i < 1:
        ask_email = input("Введите email на яндексе: ").strip()
        result = reg_check(ask_email, user_data_list)
        if result:
            print("Почта принята")
            print()
            ask_email_i += 1
        else:
            print("Почта должна содержать только латинские буквы или цифру затем @yandex.ru")
            print()


    check_unique_data(user_data_list, users_list)


for item in users_list:
    print(item)