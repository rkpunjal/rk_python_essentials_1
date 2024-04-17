# condition basics
#--------------------



# if condition :
#     1 or more spaces indentation <statement to execute when condition is satisfied>

# age = int(input("Enter your age : "))
# if age>= 21 :
#     print("Come on in!")
#     print("Find yourself a table")
# else :
#     print("Go home kid")


# Else if  (elif)
# ski_run_color = input("Enter ski run color : ")
#
# ski_run_color = ski_run_color.lower()
#
# if ski_run_color== "green" :
#     print("Beginner ski run !")
# elif ski_run_color == "blue" :
#     print("Intermediate ski run")
# elif ski_run_color == "black" :
#     print("Expert ski run")
# else :
#     print(f"'{ski_run_color}' is NOT assigned for ski runs !")



# nested conditions
# --------------------------

unit = "degree"
value = 5

# unit = "farenheit"

if unit == "degree":
    if value <= 0:
        print("It's freezing !")
    else:
        print("It's not freezing")
else:
    print("Sorry I am bad with Farenheit !")



