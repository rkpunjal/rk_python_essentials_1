
first_name = "Ramakrishna"
last_name = 'Punjal'

# if you add strings, they concatenate

full_name = first_name + last_name

print("full_name : ", full_name)

# if you multiply strings, they repeat

print("first_name * 3", first_name * 3)

# cannot multiply 2 strings

# string index
print("index 2 of 'Punjal' : ", last_name[2])


# automatically get the last index with -1 (without knowing the length of the string)
print("last index using -1 of 'Punjal' : ", last_name[-1])


# -2 is 2nd from last, -3 is 3rd from last and so forth
print("index -3 of 'Punjal' : ", last_name[-3])

# Slice String
print("first_name[4:8] : ", first_name[4:9])

print("first_name[4:] : ", first_name[4:])  # everything starting from index 4
print("first_name[:3] : ", first_name[:3])  # everything till index 3

# multi-line strings using triple quotes
greeting = """Hello
World"""
print("greeting: ", greeting)
