# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
persons = [
    {"name": "John", "age": 15},
    {"name": "Jack", "age": 25},
    {"name": "Harry", "age": 14},
    {"name": "Thomas", "age": 27},
    {"name": "Connor", "age": 55},
    {"name": "Olivia", "age": 13},
    {"name": "Amalia", "age": 13},
    {"name": "Jessica", "age": 34},
    {"name": "Scarlet", "age": 25}
]
age_list = []
name_list = []
for person in persons:
    age_list.append(list(person.values())[1])
    name_list.append(list(person.values())[0])
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
persons_dict = {}
name_list = []
age_list = []
for person in persons:
    name_list.append(list(person.values())[0])
    age_list.append(list(person.values())[1])
young_person = [name_list[index] for index, age in enumerate(age_list) if age == min(age_list)]
print(young_person)


# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
maxlength = 0
longestlist = []
for name in name_list:
    if len(name) > maxlength:
        maxlength = len(name)
        longestlist = [name]
    elif len(name) == maxlength:
        longestlist.append(name)
for item in longestlist:
    print(item)

# в) Посчитать среднее количество лет всех людей из списка.
sum_person_age = sum(age_list)
average = [sum_person_age/len(name_list)]
print('Средний возраст persons', average)


# 2) Даны два словаря my_dict_1 и my_dict_2.
my_dict_1 = {
    "name": "Nikita",
    "surname": "Fomin",
    "age": "22",
    "phone": "07785334566"
}
my_dict_2 = {
    "name": "Julia",
    "surname": "Marty",
    "car": "BMW m3",
    "job": "auto dealer"
}
# а) Создать список из ключей, которые есть в обоих словарях.
keys_list = [key for key in my_dict_1 if key in my_dict_2]
print(keys_list)
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
keys_list_1 = [key for key in my_dict_1 if key not in my_dict_2]
print(keys_list_1)
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
new_dict = {key: value for key, value in my_dict_1.items() if key in keys_list_1}
print(new_dict)
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
t_dict = my_dict_1.copy()
keys_set = set(my_dict_1.keys()) | set(my_dict_2.keys())
for key in keys_set:
    if key in my_dict_1 and key in my_dict_2:
        t_dict[key] = [my_dict_1.get(key)] + [my_dict_2.get(key)]
    elif key in my_dict_1 and key not in my_dict_2:
        t_dict[key] = my_dict_1.get(key)
    elif key in my_dict_2 and key not in my_dict_1:
        t_dict[key] = my_dict_2.get(key)
print(t_dict)
