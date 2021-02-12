num_list = int(input('Пожалуйста, введите количество элементов в списке: '))
user_list = []
while len(user_list) < num_list:
    el = input('Пожалуйста, введите элемент списка: ')
    user_list.append(el)
for el in range(1, len(user_list), 2):
    user_list[el - 1], user_list[el] = user_list[el], user_list[el - 1]
print(user_list)