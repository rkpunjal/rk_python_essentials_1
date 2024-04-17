height = int(input("Please enter your height in cm : "))
weight = int(input("please enter your kg : "))

bmi = weight / ((height*0.01)**2)

print(f"")

category = 'Un-calculated'

if bmi < 16:
    category = "Severely Underweight"
elif bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Over-weight"
elif bmi < 35:
    category = "Moderately Obese"
elif bmi < 40:
    category = "Severely Obese"
elif bmi >= 40:
    category = "Morbidly Obese"

print(f"Your BMI : '{bmi}' makes you '{category}'")

