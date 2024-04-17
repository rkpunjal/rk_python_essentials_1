
tweet = input("Enter your tweet : ")

max_length = 140

more_chars = len(tweet) - max_length

if more_chars > 0:
    print(f"Your tweet is '{more_chars}' longer than allowed '{max_length}' character")
else:
    print("Length is Ok!")
