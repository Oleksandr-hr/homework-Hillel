my_value = int(5)
value = int(input("Введи число and press Enter:"))
while value != my_value or value == my_value:
    if value > my_value:
        value = int(input("Введите число меньше"))
    elif value < my_value:
        value = int(input("Введите число больше"))
    else:
        print("ты угадал" + " " + str(5))
        print('Спасибо за игру !')
        break

str_ = input('Введите строку: ')

if len(str_) > 2:
    if str_[-3:] == 'ing':
        str_ += 'ly'
    else:
        str_ += 'ing'
print(str_)
