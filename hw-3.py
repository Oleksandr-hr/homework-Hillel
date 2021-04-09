####################################-1
value = int(input("Твое значение:"))
new_value = int(value / 2) if value < 100 else -value
print(new_value)

####################################-2
value = int(input("Твое значение:"))
new_value = "1" if value < 100 else "0"
print(new_value)

####################################-3
value = int(input("Твое значение:"))
new_value = True if value < 100 else False
print(new_value)

###################################-4
my_str = str("Твое значение:")
my_str = my_str[::2]
print(my_str)

# ###################################-5
my_str = str("Твое значение:")
my_str = my_str[1::2]
print(my_str)

####################################-6
my_str = str("Твое значение")
if len(my_str) < 5:
    print(my_str * 2)
else:
    len(my_str) > 5
    print(my_str)

####################################-7
my_str = str("Твое значение")
if len(my_str) < 5:
    print(my_str + my_str[::-1])

else:
    len(my_str) > 5
    print(my_str)