#setup
print("Welcome to the BMI/TDEE Calculator, if you want to put a comma use a period." )
import pandas as pd
import random
Boy_BMI = pd.read_csv("Boy_BMI.csv", index_col = 0)
Girl_BMI = pd.read_csv("Girl_BMI.csv", index_col = 0)
information_needed = "length_weight_age_gender"

#getting data
while information_needed == "length_weight_age_gender":
    try:
        length = float(input("What is your length in centimeters?: "))
        if length < 1:
            raise ValueError
        else:
            information_needed = "weight_age_gender"
    except ValueError:
        print("Is not a valid number. Please, only put positive numbers and use period instead of a comma.")

while information_needed == "weight_age_gender":
    try:
        weight = float(input("What is your weight in kgs?: "))
        if weight < 1:
             raise ValueError
        else:
            information_needed = "age_gender"
    except ValueError:
        print("Is not a valid number. Please, only put positive numbers and use period instead of a comma.")

while information_needed == "age_gender":
    try:
        age = float(input("What is your age? Needs to be 3 or higher: "))
        if age < 3:
            raise ValueError
        else:
            information_needed = "gender"
            age = round(age)
    except ValueError:
        print("Is not a valid number. Please, only put in a whole positive numbers. that is 2 or higher")


while information_needed == "gender":
    try:
        gender = input("What is your gender? male/female?: ")
        if gender != "male" and gender != "female":
            raise ValueError
        else:
            information_needed = "Nothing"
    except ValueError:
        print("Please, choose from male or female.")

#calculate and give the BMI
print("your length =",length, "weight =",weight,"age =",age,"gender =",gender)
BMI = round(weight/((length/100) **2 ),1)
print("your BMI =",BMI)

#tell if the BMI is low, healthy or high
if age >= 18 and age < 65:
    if BMI < 18.5:
        relative_BMI = "low"
    elif BMI < 25:
        relative_BMI = "high"
    else:
        relative_BMI = "healthy"

if age >= 65:
    if BMI < 22:
        relative_BMI = "low"
    elif BMI < 27:
        relative_BMI = "high"
    else:
        relative_BMI = "healthy"

if age < 18 and gender == "male":
    low = Boy_BMI.loc[age, "LOW"]
    high = Boy_BMI.loc[age, "HIGH"]
    if BMI < low:
        relative_BMI = "low"
    elif BMI < high:
        relative_BMI = "high"
    else:
        relative_BMI = "healthy"

if age < 18 and gender == "female":
    low = Girl_BMI.loc[age, "LOW"]
    high = Girl_BMI.loc[age, "HIGH"]
    if BMI < low:
        relative_BMI = "low"
    elif BMI < high:
        relative_BMI = "high"
    else:
        relative_BMI = "healthy"

print(f"You have a",relative_BMI, "BMI")

#tell TDEE
information_needed = "activity_level"
while information_needed == "activity_level":
    try:
        activity_level = int(input("To calculate your TDEE: amount of calories you burn in a day enter how active you are in a day from 1-5. 1 being not active and 5 being very active: "))
        if activity_level in [1, 2, 3, 4, 5]:
            information_needed = "None"
        else:
            raise ValueError
    except ValueError:
        print("Please enter a number between 1 and 5")

if activity_level == 1:
    activity_factor = 1.2
elif activity_level == 2:
    activity_factor = 1.375
elif activity_level == 3:
    activity_factor = 1.55
elif activity_level == 4:
    activity_factor = 1.725
elif activity_level == 5:
    activity_factor = 1.9

if gender == "male":
    TDEE = round((10 * weight + 6.25 * length -    5 * age + 5) * activity_factor)
else:
    TDEE = round((10 * weight + 6.25 * length - 5 * age - 161) * activity_factor)

print(f"Your TDEE is {TDEE} calories.")
