"""1. Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

user_num1 = input("First number:\n")
user_num2 = input("Second number:\n")


def my_func(num1, num2):
    if num1.isdigit() and num2.isdigit():
        num1, num2 = int(num1), int(num2)
        result = num1 / num2
        return round(result, 2)


print(my_func(user_num1, user_num2))
# ===================================================
"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

user_name = input("Enter name:\n")
user_lastName = input("Enter lastName:\n")
user_yearOld = input("Enter yearOld:\n")
user_city = input("Enter city:\n")
user_email = input("Enter email:\n")
user_phone = input("Enter phone:\n")


def user_info(name, lastName, yearOld, city, email, phone):
    return {'name': name, 'lastName': lastName,
            'yearOld': yearOld, 'city': city,
            'email': email, 'phone': phone}


print(user_info(user_name, user_lastName, user_yearOld, user_city, user_email, user_phone))
# ===================================================
"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func2(arg1, arg2, arg3): # 6, 8, 45
    args_list = [arg1, arg2, arg3]
    max_dig = max(args_list)
    args_list.remove(max(args_list))
    middle_dig = max(args_list)
    return max_dig + middle_dig


print(my_func2(2234, 123, 5))
