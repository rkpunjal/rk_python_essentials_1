# return to input() is always a string
# even if the user enters a number
# so to use it as a number, you need to convert it's type.

age_str = input("Enter your age : ")
print("Type : ", type(age_str) )

months = age_str*12
print("you are", months, "months old (age_str * 12) ")

age_int = int(age_str)
months = age_int*12
print("type( int(age_str) ) : ", months )
print("you are", months, "months old (age_int * 12)")


# similarly
# float('12.6')   # convert to float
# str(44.5)       # convert to string


