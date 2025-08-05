
# calculate BMI
# get weight in kg and height in cm
# change cm to m
# eqn for calculating bmi = weight in kg / height in cm^2

weight_in_kg = int(input("Enter your weight in kg: "))

height_in_cm = int(input("Enter your height in cm: "))

height_in_meter = height_in_cm / 100

bmi = weight_in_kg / height_in_meter**2

print("Your BMI is = ",bmi)