# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.
def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(name = 'Evgeniy', surname='Sh' year = '1996', city = 'MSK', email = '1@1.ru', telephone = '+7999-999-99-99'))