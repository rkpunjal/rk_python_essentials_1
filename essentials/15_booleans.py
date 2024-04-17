# Possible values :  True or False

findWhat_1 = "Tor"
sourceString = "Tor Arild"

print(f"Is '{findWhat_1}' in '{sourceString}'?", findWhat_1 in sourceString )

findWhat_2 = "Jonas"
print(f"Is '{findWhat_2}' in '{sourceString}'?", findWhat_2 in sourceString )


# find ASCII char number of a character
my_char = 'A'
print(f"ord of '{my_char}' = {ord(my_char)}")

my_char = 'a'
print(f"ord of '{my_char}' = {ord(my_char)}")

my_char = '.'
print(f"ord of '{my_char}' = {ord(my_char)}")

my_char = ' '
print(f"ord of '{my_char}' = {ord(my_char)}")


firstString = "apple"
secondString = "apple"
thirdString = "Apple"
fourthString = firstString

print(f"'{firstString}' == '{secondString}' : ", firstString == secondString)
print(f"'{firstString}' == '{thirdString}' : ", firstString == thirdString)
print(f"'{firstString}' is '{thirdString}' : ", firstString is thirdString)

print()
print("fourthString = firstString")
print(f"'firstString' is 'fourthString' : ", firstString is fourthString)
