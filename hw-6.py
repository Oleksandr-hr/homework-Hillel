# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

my_list = ['lorem', 'dolor', 'sit', 'amet']
new_List = []
for index, item in enumerate(my_list):
    if index % 2 !=0:
        new_List.append(item[::-1])
    else:
        new_List.append(item)
print(new_List)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
my_list = ['alex', 'qwe', 'argo', 'mys', 'arty']
too_list = []
for value in my_list:
    if value[0] == "a":
        too_list.append(value)
print(too_list)

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_list_one = ['alex', 'qwae', 'rgo', 'mysa', 'mrty', 'ta']
newLiSt = [newLiSt for newLiSt in my_list_one if "a" in newLiSt]
print(newLiSt)

# 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.
my_List = ['hello', 'post', 122, 31, "12-hobbit"]
new_List = [value for value in my_List if type(value) == str]
print(new_List)

# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
my_str = 'lorem input astrolog'
new_str = [i for i in my_str if my_str.count(i) == 1]
print(new_str)

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
my_str = 'mercedes'
my_str_2 = 'porsche'
my_result = set(my_str).intersection(set(my_str_2))
print(list(my_result))

# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
my_str_1 = 'mercedes'
my_str_2 = 'porsche'
my_result_1 = []
my_result_2 = []
for i in my_str_1:
    if my_str_1.count(i) == 1:
        my_result_1.append(i)
for i in my_str_2:
    if my_str_2.count(i) == 1:
        my_result_2.append(i)
my_result = set(my_result_1).intersection(set(my_result_2))
print(my_result)
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность
person = {
    "name": "Alex",
    "surname": "Finski",
    "age": 22,
    "accommodation":{
        "country": "Ukraine",
        "city": "Kiev",
        "street": "Haharina",
    },
    "Work" :{
        "Availability": "Yes",
        "Position": "photographer",
    }

}
print(person)
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#
#     #Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
#         Масло

napoleon_cake = {
    "Cakes": {
        "Flour": "100 gr",
        "Milk": "250 gr",
        "Butter": "25 gr",
        "Egg": "5 gr",
    },
    "Cream":{
        "Sugar": "50 gr",
        "Butter": "100 gr",
        "Vanilla": "300 gr",
        "Sour cream": "200 gr",
    },
    "Glaze":{
        "Cacao":"500gr",
        "Sugar":"100 gr",
        "Butter":"125 gr",
    },

}
print(napoleon_cake)