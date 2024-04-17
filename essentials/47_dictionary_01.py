
# dictionary_variable = {"key1": "value", "key2": value2}
product_list = {"apple": 5.2, "banana": 4.0, "mango": 7.5, "strawberry": 6.0}
# product_list = {}
# product_list = dict()

# keys can be only immutable data-types
# number, strings, booleans, etc
# eg: a list cannot be a key, but a int, string, float can be a value


# retrieving values from dictionary
print("product_list : ", product_list)
print("product_list['banana'] : ", product_list["banana"])

# update value
product_list["banana"] = 3.75
print("after update product_list['banana'] : ", product_list["banana"])

# adding more keys-values existing dictionary
# dictionary_variable["new_key"] = "new_value"
product_list["orange"] = 4.5
print("after new key, product_list : ", product_list)

# 'in' operator to know if a key exists in the dictionary
# only looks at keys not values
if "strawberry" in product_list:
    print("The 'strawberry' costs : ", product_list["strawberry"])

if "watermelon" in product_list:
    print("The 'watermelon' costs : ", product_list["watermelon"])
else:
    print("There is no 'watermelon' key")


# safer way is use '.get("key")'
# it either retrieves the value if key is present, else returns null, keyError
print("product_list.get('watermelon') : ", product_list.get('watermelon'))

print()

# remove a key
# '.pop("key")' will remove and return

mango = product_list.pop("mango")
print("product_list : ", product_list)
print("removed - mango : ", mango)


print()


# .popItem() removes the most recently added key
product_list["blackberry"] = 6.5
print("product_list            : ", product_list)
product_list.popitem()
print("after '.popItem()' : ", product_list)


print()


# del dictionary_variable["key"]
product_list["peach"] = 3.5
print("product_list              : ", product_list)
del product_list["peach"]
print("del product_list['peach'] : ", product_list)


print()

# copy
copied_list = product_list.copy()
print("product_list : ", product_list)
print("copied_list : ", copied_list)
print("product_list is copied_list : ", product_list is copied_list)

# compare if they have same contents
print("product_list == copied_list : ", product_list == copied_list)


print()
print("iterating keys")
print("----------------------------")
# iterating
product_names_list = product_list.keys()
for product in product_names_list:
    print(product)

print()

# iterating
print("iterate values")
print("----------------------------")
cost_list = product_list.values()
for cost in cost_list:
    print(cost)


print()
print("iterate and perform operations eg total")
print("----------------------------")
total_cost = 0
for cost in cost_list:
    total_cost += cost
print("total cost : ", total_cost)


print()
print("iterate through keys and get values")
print("----------------------------")
for key in product_list.keys():
    print(f"{key} : {product_list[key]}")


print()
print("dictionary.items()")
print("----------------------------")

# '.items()' get list of key-value pairs (tuple)
for item in product_list.items():
    print(item)

print()
print("directly unpack values from dictionary.items()")
print("----------------------------------------------")
costliest_fruit = ""
max_cost = 0
for fruit,cost in product_list.items():
    print(fruit, cost)
    if cost > max_cost:
        max_cost = cost
        costliest_fruit = fruit

print("costliest_fruit: ", costliest_fruit, ", max_cost: ", max_cost)


print()
print("no need to use .keys()")
print("iterate over dictionary directly gives keys")
print("----------------------------")
for key in product_list:
    print(f"{key} : {product_list[key]}")


print()

print(".update()")
# if same keys already exist, the values are replaced
print("----------------------------")
print("product_list  : ", product_list)
product_list.update({"grapes": 2.5, "plum": 2.5})
print("after .update : ", product_list)


print()

print(".merge dictionaries and create new dictionary")
print("---------------------------------------------")
d1 = {'a': 1, 'b': 2, 'd': 4}
d2 = {'c': 3, 'd': 'd-value'}
print("d1 : ", d1)
print("d2 : ", d2)

d3 = {**d1, **d2}
# if same keys already exist, the values are replaced, in the given order
print("d3 = {**d1, **d2} : ", d3)
print("{**d2, **d1} : ", {**d2, **d1})

print("---------------------------------------------")
print("'|' union / pipe operator and right-side will win in-case of duplicate keys")
print("d1 | d2 : ", d1 | d2)
print("d2 | d1 : ", d2 | d1)



print()

print("nested dictionary")
print("---------------------------------------------")
produce = {
    "strawberry" : {
        "price" : 4.5,
        "quantity" : 500,
        "organic" : True,
        "producer" : "Tropical Dream Farm"
    },
    "orange" : {
        "price" : 3.5,
        "quantity" : 200,
        "organic" : False,
        "producer" : "Della's Farm"
    }

}

print("produce : ", produce)
print("produce['orange'] : ", produce['orange'])
print("produce['orange']['producer'] : ", produce['orange']['producer'])

