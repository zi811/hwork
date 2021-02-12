goods = []
features = {'название': '', 'цена': '', 'количество':'', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество':[], 'единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        pro = input(f'Введите значение свойства "{f}": ')
        features[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        analytics[f].append(features[f])
    goods.append((num, features))
    print(f'\nСтруктура товаров\n{goods}')
    print(f'\nТекущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print('*' * 30)