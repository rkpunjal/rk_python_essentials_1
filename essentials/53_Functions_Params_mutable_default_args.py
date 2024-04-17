# if you have a default mutable parameter (eg: list)
# it will be re-used for subsequent calls
# this does-not happen for non-default mutable parameters


def add_twice(phrase, my_list=[]):
    my_list.append(phrase)
    my_list.append(phrase)
    return my_list


the_list = add_twice('yay')
print("the_list : ", the_list)
# result = the_list :  ['yay', 'yay']

the_list = add_twice('boo')
print("the_list : ", the_list)
# result = the_list :  ['yay', 'yay', 'boo', 'boo']

# we were expecting only : ['boo', 'boo']
# system used param 'my_list' again (in previous state)

print()
print()


# to prevent this, we can initialize it to None and initialize later in the function


def add_thrice(phrase, my_list=None):
    if my_list == None:
        my_list = []

    my_list.append(phrase)
    my_list.append(phrase)
    my_list.append(phrase)
    return my_list


the_list = add_thrice('yay')
print("the_list : ", the_list)
# result = the_list :  ['yay', 'yay', 'yay']


the_list = add_thrice('boo')
print("the_list : ", the_list)
# result = the_list :  ['boo', 'boo', 'boo']   -- as expected

