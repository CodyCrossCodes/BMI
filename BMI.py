height = float(input("Enter your height in meters: "))

weight = float(input("Enter your weight in kilograms: "))

bmi = weight / height**2
bmi_string = str(round(bmi, 1))

if bmi < 18.5:
    print(f"Your BMI is {bmi_string}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi_string}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi_string}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi_string}, you are obese.")
else:
    print(f"Your BMI is {bmi_string}, you are clinically obese.")
  