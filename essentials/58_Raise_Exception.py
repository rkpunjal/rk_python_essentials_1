print("----------------------------------")
print("Raise Exceptions : (Try negative number) ")
print("----------------------------------")

try:
    num = int(input("Enter a number : "))

    if num < 0:
        # raise ValueError   # without message
        raise ValueError(f"You entered a Negative Number '{num}' !")   # with message

except ValueError as ve:
    print(ve)
    print("That was not a valid number!")
    print("I'll pick for you .... 7")
    num = 7
except EOFError:
    print("You didnot enter anything!")
    print("Your number will be 0")
    num = 0

print("Your number : ", num)



