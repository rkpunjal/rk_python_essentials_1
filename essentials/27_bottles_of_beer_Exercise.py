
# Bottles of beer - Exercise

# using for

print("---------------------------------------")
print("using for and range")
print("---------------------------------------")
for num in range (10, 0, -1):
    print(f"{num} bottles of beer on the wall.")
    if num-1 > 0:
        print(f"Take one and pass along, {num-1} bottles of beer on the wall.")
    else:
        print("Take one and pass along, No more bottles of beer on the wall.")

    print("*********************************")


print("---------------------------------------")
print("using while")
print("---------------------------------------")

bottles = 10
while bottles > 0:
    print(f"{bottles} bottles of beer on the wall.")
    if bottles-1 > 0:
        print(f"Take one and pass along, {bottles-1} bottles of beer on the wall.")
    else:
        print("Take one and pass along, No more bottles of beer on the wall.")

    bottles -= 1
    print("*********************************")

