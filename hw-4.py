#1
my_list = [101, 99, 250, 36, 106, 6]
for new_list in my_list:
    if new_list > 100:
        print(new_list)
#2
my_list = [101, 99, 250, 36, 106, 6, 222, 33, 515]
my_result = []
for i in my_list:
    if i > 100:
        my_result.append(i)
print(my_result)
#3
my_list = [101, 99, 250, 111]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)
#4
my_string = '0123456789'
new_lst = []
for a in my_string:
    for b in my_string:
        new_lst.append(int(a + b))
print(new_lst)