
# Inheritance syntax:
# ----------------------------
# class name_of_class(parent_class_name):
#     def member_methods(self):
#

class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} Meows !!!")


# -------------------------

class Lion(Cat):

    def __init__(self, name, pride):
        super().__init__(name)  # call super class constructor
        self.pride = pride

    def roar(self):
        print(f"{self.name} Roars !!!")


# -------------------------

class Cougar(Cat):
    def __init__(self, name):
        super().__init__(name)  # call super class constructor

    def purr(self):
        print(f"{self.name} Purrs !!!")

# -------------------------



mika = Cat('Mika')
mika.meow()

print()

eli = Lion('Eli', "Rulers")
eli.meow()  # inherited method
eli.roar()  # specialized method
print("eli.pride : ", eli.pride)  # specialized variable


print()

jumpy = Cougar('Jumper')
jumpy.meow()  # inherited method
jumpy.purr()  # specialized method
