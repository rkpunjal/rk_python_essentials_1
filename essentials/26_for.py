
# for

# syntax
# ------------
# for item in iterable:
#   statement

my_word = "Hello"

for char in my_word:
    print(char)

print("-------------------")


# 'range' syntax
# -----------------
# for item in range(start, stop, <step>):
#   statement
print("using range, no step")

for num in range(1, 10):
    print(num)

print("-------------------")

print("using range, with step")

for num in range(1, 10, 2):
    print(num)



print("-------------------")

print("using range, no start, no step")

for num in range(10):
    print(num)



print("-------------------")

print("using range, backwards with negative step")
for num in range(10, 0, -1):
    print(num)
