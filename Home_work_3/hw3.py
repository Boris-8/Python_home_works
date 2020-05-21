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
