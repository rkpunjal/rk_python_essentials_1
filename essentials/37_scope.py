
# scope

# L.E.G.B.
# L = Lexcial /locak   = local
# E = Enclosing  = inside functions / loops / conditions
# G = Global     = global
# B = Built-in   = all built-in functions/variables

print("----------------------------")
print("   Global Scope")
print("----------------------------")

# Global
# ----------------

animal = "lemur"

print("out-side any function : ", animal )

print()
print()


print("----------------------------")
print("   local Scope")
print("----------------------------")


def my_func():
    print("inside my_func : ", animal)
    out_func_animal = "seal"

    def inner_func():
        print("inside inner_func : ", animal)
        print("outer func-variable in inner_func : ", out_func_animal)

    inner_func()



my_func()

# animal can be accessed even inside the functions as it is global



def zoo():
    zoo_animal = "zebra"
    print("iside zoo : ", zoo_animal)


zoo();
# print(zoo_animal)   # can't access zoo_animal as it is local only to that function
# variables declared inside a function are local to that function only

print()
print()


print("----------------------------")
print("   Loop & Condition Scope")
print("----------------------------")

# **** SPECIAL
# variables declared inside IFs or LOOPs are accessible outside that block

for ch in "BLUE":
    loop_animal = "OCTOPUS"
    print(ch)

print("loop_animal : ", loop_animal)
print("ch looping char: ", ch ) # the 'ch' looping variable is also accessible

if True:
    condition_animal = "penguin"

print("condition_animal : ", condition_animal)


print()
print()


print("----------------------------")
print("   access level") # LEGB
print("----------------------------")


water_animal = "shark"

def my_func():
    water_animal = "squid"
    print("inside my_func : ", water_animal)


my_func()

print("outside : ", water_animal )

