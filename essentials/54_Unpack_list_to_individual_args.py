# unpack a list into individual arguments

def average(*nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)


print("average(1,2,3,4,5) : ", average(1, 2, 3, 4, 5))

my_nums = [1, 2, 3, 4, 5]  # list of
# print("average : ", average(my_nums))   # TypeError: unsupported operand type(s)
print("average : ", average(*my_nums))  # '*' before list-variable-name converts it to individual params

print()
print("Create new list include existing list + more ")
print("----------------------------------------------------")
# create a new list including the existing values from existing list and some more
new_nums = [*my_nums, 6, 7, 8]
print("my_nums : ", my_nums)
print("new_nums = [*my_nums, 6, 7, 8]")
print("new_nums : ", new_nums)

