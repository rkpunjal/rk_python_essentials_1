
# default params
# assign a value to it to make it a parameter
print("---------------------------")

def laugh(intensity = 2):
    print("Ha!"*intensity)


laugh(10)
laugh()

print("---------------------------")


def slugify(message, separator="-"):
    return str(message).strip().replace(" ", separator)

the_string = "hello world I LOVE YOU"
separator = "_"
print(f"slugify('{the_string}') : {slugify(the_string)}")
print(f"slugify('{the_string}', '{separator}') : {slugify(the_string, separator)}")


print("---------------------------")

# default parameters should come after non-default params (NOT before)

def greet(name, phrase="Hi") :   # fails for -->  def greet(phrase="Hi", name) :
    print(phrase,name)


greet("John");
greet("Maria", "Hello")

print("---------------------------")

# named-args = keywords
def get_total(price, qty=1, tax=0.02, discount=0):
    subtotal = price * qty * (1-discount)
    print(subtotal * (1+tax))

print("no param names : ")
get_total(5, 5, 0.015, 0.2)

print("")

print("using named-params : ")
get_total(price=5, qty=5, tax=.015, discount=0.2)


print("")

print("using named-params with different sequence ")
get_total(price=5, discount=0.2, qty=5, tax=0.015)


print("")

print("using named-params using fewer params beause of default-param-values ")
get_total(5, tax=0.015)


