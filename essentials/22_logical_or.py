
# logical 'or' operator

day = input("Enter a day of the week : ")

day = day.lower()
if day == "saturday" or day == "sunday":
    print("It's a week-end!")
else:
    print("Not a week-end")


