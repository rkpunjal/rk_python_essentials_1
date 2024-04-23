# Class - Syntax
# ----------------------
# class Class_name:
#     class_level_variable

#      @classMethod
#        my_class_method(cls):
#           <do something>

#     def __init__(self, <params>):
#         # optional - initialize the member variables

#         # instance variable = self.
#         self.param1 = param1
#         self.param2 = param2

# class level variable
#         Class_name.variable_name

class Dog:
    # class variable
    number_of_dogs = 0

    # constructor
    def __init__(self, name, breed, location):
        # instance variables
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        Dog.number_of_dogs += 1

    @classmethod
    def print_num_of_dogs(cls):
        print(f"Number of Dogs registered : {Dog.number_of_dogs}")

    # call constructor and return instance
    @classmethod
    def register_stray(cls):
        return cls("Coming Soon", "Coming Soon", "Coming Soon")

    def bark(self):
        print(f"{self.name} says WOOF!")

    def learn_trick(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)

    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs '{trick}'")
        else:
            print(f"{self.name} does not know '{trick}'")


# -----------------------------------

otter = Dog("Otter", "Husky", 210035)
tina = Dog("Tina", "Pomerian", 210091)

print("type(otter) : ", type(otter))
print("otter.name : ", otter.name)
print("otter.breed : ", otter.breed)
print("otter.location : ", otter.location)

print()

print("otter.bark()")
otter.bark()

print("tina.bark()")
tina.bark()

print()

print("otter.tricks : ", otter.tricks)

otter.learn_trick('sit')
print("otter.tricks : ", otter.tricks)

otter.learn_trick('stay')
print("otter.tricks : ", otter.tricks)

print()

print("tina.tricks : ", otter.tricks)

tina.learn_trick('spin')
print("tina.tricks : ", tina.tricks)

tina.learn_trick('stay')
print("tina.tricks : ", tina.tricks)

print()
otter.perform_trick("sit")
otter.perform_trick("spin")

print()
print("Number of Dogs : ", Dog.number_of_dogs)

homer = Dog("Homer", "German Shepard", 22000145)
print("Number of Dogs : ", Dog.number_of_dogs)


print()
print("Dog.register_stray()")
stray = Dog.register_stray()
print("stray.name : ", stray.name)
print("stray.breed : ", stray.breed)
print("stray.location : ", stray.location)
