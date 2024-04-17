
myString = "eggPlant";
print("original : ", myString)
print("myString.lower() : ", myString.lower())
print("myString.upper() : ", myString.upper())
print("myString.capitalize() : ", myString.capitalize())

print("=====================================")

print(".strip(),   .strip([chars]),  .lstrip([chars]),   .rstrip([chars])")
myString = "     Hello World        "
print("\"" + myString + "\".strip() : " + "\"" + myString.strip() + "\"" )

# strip() also removes all white spaces, \n, \t, \t

print("\n")
myString = "     Hello World     How are you?   "
print("\"" + myString + "\".strip() : " + "\"" + myString.strip() + "\"" )
print("\n")

myString = ",.,.,.,.,Hello World,.,.,.,."
print("\"" + myString + "\".strip(',.') : " + "\"" + myString.strip(',.') + "\"" )
print("\"" + myString + "\".lstrip(',.') : " + "\"" + myString.lstrip(',.') + "\"" )
print("\"" + myString + "\".rstrip(',.') : " + "\"" + myString.rstrip(',.') + "\"" )


print("=====================================")

myString = "3 kilometers, 5 kilometers, 10 kilometers, 15 kilometers"
print("original : ", myString)
print("using replace : ", myString.replace("kilometers", "km"))


print("\n")

myString = "$3.5, $5.5, $10.5, 15$.50"
print("original : ", myString)
print("remove $ using replace with ''  .replace('$', '') : ", myString.replace('$', ''))

print("remove $ using replace with '', only 2 occurences(3rd param)  .replace('$', '', 2) : ", myString.replace('$', '', 2))


print("\n")

print("=====================================")


#  find - will give the 1st index of the param
myString = "3 kilometers, 5 kilometers, 10 kilometers, 15 kilometers"
print("original : ", myString)
print(".find('kilometers') : ", myString.find('kilometers'))
print(".count('kilometers') : ", myString.count('kilometers'))



print("\n")

print("=====================================")

# method chaining

my_email = "TODD@gmail.com   "
print(f"original : '{my_email}'")
print("my_email.lower().strip() : '" + my_email.lower().strip() + "'")

