with open('test5.3.txt', 'r') as my_file:
    surname = []
    sum_pay = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           surname.append(i[0])
        sum_pay.append(i[1])
print(f' ЗП меньше 20.000: {surname}\n Всего {len(surname)} человек \n Средняя ЗП: {sum(map(int, sum_pay)) / len(sum_pay)}')