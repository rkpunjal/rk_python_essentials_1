
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
print("----------------------------------")
print("    using for")
print("----------------------------------")
for char in word:
    print(char)

print("----------------------------------")
print("    using while")
print("----------------------------------")

# Write a while loop that does the same thing!
index = 0
while index < len(word):
    print(word[index])
    index += 1

print("----------------------------------")
#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)

print("----------------------------------")
print("    while - print even numbers between 100 to and including 140 ")
print("----------------------------------")

num = 100
while num <= 140:
    print(num)
    num += 2



# Write a for loop that does the same thing (with range())
print("----------------------------------")
print("    for - print even numbers between 100 to and including 140 ")
print("----------------------------------")

for num in range(100, 141, 2):
    print(num)

print("----------------------------------")

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:

passphrase = ""

while passphrase != "sillygoose":
    passphrase = input("Type 'sillygoose' : ").lower()

print("----------------------------------")



