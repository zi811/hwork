proceeds = int(input('Какова выручка вашей фирмы? '))
costs = int(input('Каковы издержки вашей фирмы? '))

if proceeds > costs:
    print('Ваша выручка превысила издержки. Поздравляем вы в плюсе на:', (proceeds-costs))
elif proceeds == costs:
    print('Вы вышли в ноль')
else:
    print('Ваши издержки, превысили выручку вы работаете в убытки')