
# Logical 'and' operator

print("Welcome to the Bar !")
age = int(input("Enter your age : "))

if age < 18:
    print("Go home kid")
elif age >= 18 and age < 21:
    print("You can enter the venue but cannot drink")
elif age >= 21:
    print("You can have drinks")


