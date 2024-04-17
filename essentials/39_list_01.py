
# Lists are ordered collection of values
# eg Lists of weekdays, medicines for the week, top_scores, tasks

#tasks = list()

tasks = ["Trash", "Dishes", "Laundry", "Dinner"]
print(tasks)
print("tasks[1] : ", tasks[1])

print()

high_scores = [98, 76, 54, 33, 21]
print(high_scores)
print("high_scores[2] : ", high_scores[2])

print()

# also possible to mix-up data-types
stuff = [4, 5.6, True, "myString", []]  # can have a list within a list
print(stuff)

print()

myStringList = list("hello") # creates a list of all characters in the string
print(myStringList)

print()

number_list = list(range(3, 10)) # using a range to create a list
print(number_list)


# changing elements in a list
number_list[0] = 15
print("changed 0th index element to 15: ", number_list);

# cannot add to list by direct value assignment like :
# myNumberList[7] = 25 # IndexError: list assignment index out of range

print("last element of list using -1 : myNumberList[-1] : ", number_list[-1])

print()

# .append() to add elements to list
nums = [1,2,3,4]
print(nums)
nums.append(5)
print("after .append(5) : ", nums)


print()


# .extend() to add multiple elements to list

waiting_list = ["jua", "aria", "amir", "rosa"]
print("wait_list : ", waiting_list)
more_people = ["charlie", "drew", "emi"]
waiting_list.extend(more_people)
print("updated wait_list : ", waiting_list)


print()


# .insert(index, element) to insert element in a list at a particular index
waiting_list.insert(1, "inserted_person")
print("updated wait_list (check index-1) : ", waiting_list)


print("")


# slice a list
# list[start-index : end-index : <step>]
print("slice a list - waiting_list[2:4] : ", waiting_list[2:4])
print("[:4] same as [0:4] - waiting_list[:4] : ", waiting_list[:4])
print("every alternate element - waiting_list[::2] : ", waiting_list[::2])


print("")
print("update a list using slice")
print("------------------------------")

# update a list (insert elements) using a slice
nums = [4,5,6,7]
print("original nums : ", nums)
nums[1:3] = ['a','b']
print("updated using nums : ", nums)
nums[1:3] = ['a','b','c','d']
print("put more elements than slice size : ", nums)
nums[1:5] = [5]
print("put less elements than slice size : ", nums)



print("")
print(".clear() to clear a list")
print("------------------------------")
nums.clear()
print("after .clear() nums : ", nums)


print("")
print(".remove(<matching-value>)")
print("------------------------------")
langs = ["Python", "Javascript", "Java", "C", "C++"]
print("original langs : ", langs)
langs.remove('Javascript')
print("after langs.remove('Javascript') : ", langs)


print("")
print(".pop() to remove 'and return' last element")
print("------------------------------")
print("current langs : ", langs)
langs.pop()
print("after langs.pop() : ", langs)


print("")
print(".pop(<index-to-remove>) to remove 'and return' element with that index")
print("------------------------------")
print("current langs : ", langs)
langs.pop(1)
print("after langs.pop(1) : ", langs)


print("")
print("del list_variable[(]<index-to-remove>] to remove element with that index")
print("------------------------------")
print("current waiting_list : ", waiting_list)
del waiting_list[1]
print("after del waiting_list[1] : ", waiting_list)
# list[2:] - delete all elements from index 2
# list[::2] - delete every other element




