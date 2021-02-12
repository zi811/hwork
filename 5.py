my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
user_answer = int(input("Введите число (для выхода введите 911): "))
while user_answer != 911:
    for el in range(len(my_list)):
        if my_list[el] == user_answer:
            my_list.insert(el + 1, user_answer)
            break
        elif my_list[0] < user_answer:
            my_list.insert(0, user_answer)
        elif my_list[-1] > user_answer:
            my_list.append(user_answer)
        elif my_list[el] > user_answer and my_list[el + 1] < user_answer:
            my_list.insert(el + 1, user_answer)
    print(f"текущий список - {my_list}")
    user_answer = int(input("Введите число (для выхода введите 911): "))