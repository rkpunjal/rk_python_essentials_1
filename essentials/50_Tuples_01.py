
# Tuples
# underpowered lists, ordered collection of different indexed elements, "Immutable"
# ---------------------------------------------
# why use Tuples ?
# more efficient than Lists, use where data shouldn't change
# dict.items() returns tuples
# can be used as keys in a dictionary (immutable)
# ---------------------------------------------

dishes = ("taco", "burger", "pizza", "fajita")
print("type(dishes) : ", type(dishes))
print("dishes : ", dishes)

t = tuple()
t = ()

# special syntax for single value initialized tuples
# single_tuple = ("first_value")   #  this doesn't work, () is interpreted as parenthesis
single_tuple = "first_value",      # notice the trailing comma
single_tuple = ("first_value",)    # notice the trailing comma inside parenthesis

print()

colors = ("red", "orange", "yellow", "blue", "green")
print("colors : ", colors)
print("len(colors) : ", len(colors))
print("colors[1] : ", colors[1])

# slice
print("slice : colors[:2] : ", colors[:3])

# Immutable :    TypeError: 'tuple' object does not support item assignment
# colors[0] = "grey"

# get index using value
print("colors.index('yellow') : ", colors.index('yellow'))

# count of occurences of a value
print("colors.count('blue') : ", colors.count('blue'))
print("non-existant - colors.count('purple') : ", colors.count('purple'))    # non existing value, count = 0

# verify existance of a value
print("'blue' in colors : ", 'blue' in colors )
print("'purple' in colors : ", 'purple' in colors )

print()

print("Iterate over tuple values")
print("----------------------------------")
for val in colors:
    print(val)
print("----------------------------------")

# cannot assign new value to elements in tuple
# *** BUT if there is a mutable object in a tuple, you can modify that mutable object (eg: list)

print()

print("IMMUTABLE - But change 'Mutable' object in tuple")
print("--------------------------------------------------")
some_tuple = (1,2,['a', 'b'],3)
print("some_tuple : ", some_tuple)
some_tuple[2].extend(['c', 'd'])
print("after modifying some_tuple[2] : ", some_tuple)

