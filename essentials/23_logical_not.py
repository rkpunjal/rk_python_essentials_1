
# logical 'not'

# will negate the existing boolean value

print (not True)
print (not 5<6)

print("----------------------------")

print("Error handling for non-numeric entry using 'not' !")
birthYear = input("Enter your birth-year : ")

if not birthYear.isnumeric():
    print("That was not a number!")
else:
    print(f"You are '{2024-int(birthYear)}' years old")


# operator precedence
# ---------------------------
# () parenthesis first
# not
# and
# or



