# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но
# с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def arg_func (*args):
    words = input("Введите слова маленькими буквами: ")
    print(words.title())
    return
arg_func()

