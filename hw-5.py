# Задание №1. Дано целое число (int). Определить сколько нулей в этом числе.
number = int(input('Your number:'))
zero_count = str(number).count('0')
print(zero_count)

# Задание №2.1 Дано целое число (int). Определить сколько нулей в конце этого числа.
# Например для числа 1002000 - три нуля
n = int(input('Your number:'))
if (n == 0):
    print(1)
    exit()
countZero = 0
while (n % 10 == 0):
    n //= 10
    countZero += 1
print(countZero)

# Задание №2.2 Дано целое число (int). Определить сколько нулей в конце этого числа.
# Например для числа 1002000 - три нуля
my_value = int(input('Your number:'))
zero = 0
while my_value % 10 == 0:
    zero += 1
    my_value //= 10
print(zero)

# Задание №3 Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить элементы на четных местах из my_list_1,
# потом все элементы на нечетных местах из my_list_2.
even_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_result = even_list[::2] + odd_list[1::2]
print(my_result)

# Задание №4
# Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1].
my_list = [88, 15, 66, 45, 19, 95, 14]
new_list = my_list[1:] + my_list[:1]
print(new_list)

# Задание №5
# Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
my_list = [88, 15, 66, 45, 19, 95, 14]
my_list.append(my_list.pop(0))
print(my_list)

# Задание №6
# Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit).
example = "43 больше чем 34 но меньше чем 56"
parts = example.split()
result = []
for value in parts:
    if value.isdigit():
        result.append(int(value))
res = sum(result)
print(res)

# Задание №7
# Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
my_string = "My long string"
left_limit = "o"
right_limit = "g"

left_index = my_string.find(left_limit)
right_index = my_string.rfind(right_limit)
res = my_string[left_index + 1 : right_index]
print(res)
####################################
# Задание №8
# Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
my_str = str(input('Enter here:'))
if len(my_str) % 2:
    my_str += "_"
result = []
for index in range(len(my_str) // 2):
    index = index * 2
    new_str = my_str[index: index + 2]
    result.append(new_str)
print(result)
####################################
# Задание №9
# Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
my_list = [2,4,1,5,3,9,0,7]
res = 0

for index in range(len(my_list)):
    if index in [0, len(my_list) - 1]:
        continue
    if my_list[index] > my_list[index - 1] + my_list[index + 1]:
        res += 1
print(res)