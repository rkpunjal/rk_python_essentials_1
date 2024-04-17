first_name = input("Enter first name : ")
last_name = input("Enter last name : ")

name_length = len(first_name) + len(last_name)

if name_length == 12:
    print(f"'{first_name + ' ' + last_name}' is exactly as long as an Average American name !")
elif name_length < 12:
    print(f"'{first_name + ' ' + last_name}' is shorter than an Average American name !")
else:
    print(f"'{first_name + ' ' + last_name}' is longer than an Average American name !")


