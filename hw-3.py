####################################-1
value = int(input("Твое значение:"))
new_value = value / 2 if value < 100 else value * (-1)
print(new_value)

####################################-2
value = int(input("Твое значение:"))
new_value = 1 if value < 100 else 0
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

# ####################################-6
my_str = str(input("Enter here:"))
new_str = my_str * 2 if len(my_str) < 5 else my_str
print(new_str)

######################################-7
my_str = str(input("Enter here:"))
new_str = (my_str + my_str[::-1]) if len(my_str) < 5 else my_str
print(new_str)