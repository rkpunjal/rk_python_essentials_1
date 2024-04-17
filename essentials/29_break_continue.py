
# 'break' keyword to exit the loop
for char in "pickleface":
    if char == 'f':
        break;
    print(char)

print("after loop")

print("---------------------------------")

# 'continue' keyword to skip current iteration of loop and go to next iteration
for char in "fatcat":
    if char == "a":
        continue
    print(char)
print("after loop")

print("---------------------------------")

for char in "supercalifragilisticexpialidocious":
    if char in "aeiou": # if any vowel
        continue
    print(char)
print("after loop")

