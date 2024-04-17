
# functions - return values

def divide(x, y):
    if x == 0:
        return "Don't divide Zero by something!"
    elif y == 0:
        return "Don't Divide by Zero!"

    return x/y

# val = divide(9, 3)
val = divide(1, 3)
# val = divide(0, 3)
# val = divide(1, 0)
# val = divide(1, 3)

print("value : ", val)


