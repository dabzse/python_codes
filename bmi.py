print("BMI calculator")
print("="*16)
height = int(input("Enter your height (cm): "))
height = float(height) / 100
weight = int(input("Enter your weight (kg): "))

bmi = weight / (height**2)
print(f"Your BMI is: {round(bmi, 3)}")

if bmi < 18:
    print("You have thin body.")
elif 18 <= bmi <= 25:
    print("You have normal body shape.")
elif 25 < bmi < 30:
    print("You are overweight.")
else:
    print("You are obese (fattened).")
