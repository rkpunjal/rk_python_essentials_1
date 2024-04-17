
birthday = "31/01/1986"
birthday_elements = birthday.split("/")
print("'31/01/1986'.split('/') = ", birthday_elements)

new_birthday = "-".join(birthday_elements)
print("'-'.join(['31', '01', '1986']) = ", new_birthday)
