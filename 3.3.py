# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3
print(f'Результат: {my_func(int(input("Введите 1-ый аргумент: ")), int(input("Введите 2-ой аргумент: ")), int(input("Введите 3-ий аргумент: ")))}')