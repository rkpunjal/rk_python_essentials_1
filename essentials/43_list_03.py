
import copy

# '+' operator, new merged list
new_list = [1,2,3] + [4,5,6]
print("[1,2,3] + [4,5,6] : ", new_list)

print()

# '*' operator, new list by repeating elements of list those many times
multiplied_list = [1,2,3] * 3
print("[1,2,3] * 3 : ", multiplied_list)

print()


# 'in' operator to determine presence of value in a list

flavours = ["chocolate", "vanilla", "lemon", "strawberry"]
print("Available Flavours : ", flavours)
response = "vanilla"
while response.lower() not in flavours:
    response = input("What flavour would you like? : ")

print(f"{response}-Icecream coming right up!")


print()

# 'count(value)'  if not found, returns 0
langs = ["Python", "C", "Javascript", "C"]
print("langs : ", langs)
print("langs.count('C') : ", langs.count('C'))
print("langs.count('Java') : ", langs.count('Java'))

print()

nums = [1,2,3,4,5,6]
print("nums : ", nums)
nums.reverse()
print("nums after '.reverse()' : ", nums)


print()

# .sort()
random_nums = [1,5,2,4,6,3]
print("random_nums : ", random_nums)
random_nums.sort()
print("nums after '.sort()' : ", random_nums)

random_colors = ["blue", "amber", "purple", "orange", "Z"]
print("random_colors : ", random_colors)
random_colors.sort()
print("random_colors after '.sort()' : ", random_colors)

print()

# '==' comparison
print("[1,2,3] == [1,2,3] : ", ([1,2,3] == [1,2,3]) )
print("[1,2,3] == [3,2,1] : ", ([1,2,3] == [3,2,1]) )

# 'is' operator checks if it's the same object (in mem)
# id(my_obj) gives id of the obj


# 'copy' a list - shallow copy (sub objects will not be copied, but only reference copied)
list1 = [1,2,3,4]
list2 = list1 # this is not copy, list1 and list2 point to the same entity
print("id(list1) : ", id(list1), ", id(list2) : ", id(list2))

list1_copy = list1.copy()
print("list1 : ", list1, ", list1_copy : ", list1_copy)
print("id(list1_copy) : ", id(list1_copy))

# use slice to copy
list1_other_copy = list1[:]   # (0 to end-index)


complex_list = [1, 2, 3, ['a', 'b', 'c']]

# deep copy - copy nested structures
complex_list_deep_copy = copy.deepcopy(complex_list)

