
my_color = [245,25, 56]

# unpack the list into individual variables in a single go
# you need to have same number of variables as many elements in the list being unpacked
red, green, blue = my_color

print("my_color : ", my_color)
print("red: ", red, ", green : ", green, ", blue : ", blue)



# '*' for multiple values
item = [4, "Pizza", "Plain", 16.99]
print("item : ", item)

quantity, *others, price = item
print("quantity : ", quantity, ", others : ", others, ", price : ", price)

print()

participants = ["bill", "ted", "tammy", "jimbo", "billibob", "pierre"]
gold, silver, bronze, *losers = participants
print("participants : ", participants)
print("gold : ", gold)
print("silver : ", silver)
print("bronze : ", bronze)
print("losers : ", losers)

