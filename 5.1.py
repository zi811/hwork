my_f = open('test5.1.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('test5.1.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()

