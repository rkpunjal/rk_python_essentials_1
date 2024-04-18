# try:
#   .....
#   <code that could generate error>
#   .....
# except:
#   <code that runs if error raised>

# Common Errors
# SyntaxError NameError
# IndexError  TypeError
# ValueError  KeyError



# 'except:' will handle all types of Exceptions / Errors
# ValueError : in-case of non-numeric entry
# EOFError : in-case of no-entry (Ctrl+D)
print("----------------------------------")
print("Basic Exception Handling : (Try 'asdf') ")
print("----------------------------------")
try:
    num = int(input("Enter a number : "))
except:
    # logging.exception("An exception was thrown!")   # using logging
    print("That isn't a number!")
    print("I'll pick for you .... 7")
    num = 7

print("Your number : ", num)


# get and print details of exception
print("----------------------------------")
print("Exception Details : (Try 'asdf') ")
print("----------------------------------")

try:
    num = int(input("Enter a number : "))
except Exception as e:  # get the exception into variable e
    # print("Exception : ", e)
    print("More Details : ")
    print(f"{type(e).__name__} : : {e}\n at line {e.__traceback__.tb_lineno} of {__file__}")
    # print(f"Exception Name: {type(e).__name__}")
    # print(f"Exception Desc: {e}")
    # print(f"Line: {e.__traceback__.tb_lineno}")
    # print(f"File: {__file__}")


# It's better to NOT handle generic Exception, but handle specific Exceptions
print("----------------------------------")
print("Handling specific Exceptions : (Try Ctrl+D) ")
print("----------------------------------")

try:
    num = int(input("Enter a number : "))
except ValueError:
    print("That was not a valid number!")
    print("I'll pick for you .... 7")
    num = 7
except EOFError:
    print("You didnot enter anything!")
    print("Your number will be 0")
    num = 0

print("Your number : ", num)



