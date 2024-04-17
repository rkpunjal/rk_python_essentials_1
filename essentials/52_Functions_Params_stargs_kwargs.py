# *args
# accept any number of arguments
# encapsulates multiple number of arguments to a function
# *args collects all arguments into a tuple

# min takes any number of params
print("min(2,4,6) : ", min(2, 4, 6))
print("min(2,4,6,-1,-4,22) : ", min(2, 4, 6, -1, -4, 22))

print()


def average(*args):
    if args == None:
        return 0

    total = 0
    for num in args:
        total += num

    return total / len(args)


print("average(2,4,8) : ", average(2, 4, 8))
print("average(2,4,8,12,16,5) : ", average(2, 4, 8, 12, 16, 5))

print()


# first and second are mandatory params, others are optional and are collected in others
def other_func(first, second, *others):
    print("first  :", first)
    print("second :", second)
    print("others :", others)


other_func(1, 2, 3, 4, 5, 6)

print()
print("--------------------------------------------------------")
print("**kwargs : variable number of keyword arguments")
print("--------------------------------------------------------")


# *kwargs
# accept any number of keyword arguments
# variable keywords arguments into dictionary

def demo_kwargs(**kwargs):
    print("kwargs :", kwargs)


# cannot call as: demo_kwargs(12)
# need to use keywords
demo_kwargs(age=12, name="john")
demo_kwargs(age=12, name="john", favcolor="blue")

print()


def print_ages(**ages):
    for k, v in ages.items():
        print(f"{k} is {v} years old")


print("print_ages(ram=43, will=54, smith=23) : ")
print_ages(ram=43, will=54, smith=23)

print()
print("--------------------------------------------------------")
print("params order")
print("--------------------------------------------------------")



# parameters order
# --------------------
# expected sequence:
# parameters, *args, default=parameters
# parameters, *args, default=parameters, **kwargs

def display_info(person, *args, status="single"):
    print("person :", person)
    print("args :", args)
    print("status :", status, " (defautl value 'single')")

print("display_info('ram', 43, 'working', 'software') :")
display_info('ram', 43, 'working', 'software')

print()

print("display_info('ram', 43, 'working', 'software', status='married') :")
display_info('ram', 43, 'working', 'software', status='married')

print()

print("display_info('ram', 43, 'working', 'software', 'married') :")
display_info('ram', 43, 'working', 'software', 'married')

print("---------------------")
print(" using **kwargs")
print("---------------------")

def display_more_info(person, *args, status="single", **kwargs):
    print("person :", person)
    print("args :", args)
    print("status :", status, " (defautl value 'single')")
    print("kwargs :", kwargs)

print("display_more_info('ram', 43, 'working', 'software', weight=57, surname='punjal' ) :")
display_more_info('ram', 43, 'working', 'software', weight=57, surname='punjal')

print()

print("display_more_info('ram', 43, 'working', 'software', weight=57, surname='punjal', status='married'  ) :")
display_more_info('ram', 43, 'working', 'software', weight=57, surname='punjal', status='married')



