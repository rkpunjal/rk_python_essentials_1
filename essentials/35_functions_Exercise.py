
# functions practice
# ------------------------

def is_even(the_num):
    if the_num % 2 == 0:
        return True
    else:
        return False

the_num = 17

print(f"is_even({the_num}) : {is_even(the_num)}")


# ---------------------------------------------

def slugify(the_string):
    return str(the_string).strip().lower().replace(" ", "-")

the_string = "hello world I LOVE YOU"

print(f"slugify('{the_string}') : {slugify(the_string)}")


# ---------------------------------------------


def count_vowels(vowel_string):

    vowel_counter = 0

    if vowel_string == None:
        return 0

    vowels = "aeiou"

    for ch in vowel_string:
        if ch in vowels:
            vowel_counter += 1

    return vowel_counter


vowel_string = "hello world I LOVE YOU"

print(f"count_vowels('{the_string}') : {count_vowels(the_string)}")

