print("BMI calculator :: improved version")
print("=" * 42)

height_ok = False
while not height_ok:
    try:
        height = int(input("Enter your height (cm): "))
        if 0 < height < 301:
            height_ok = True
        else:
            print("Please enter a valid height between 1 and 300 cm.")
    except ValueError:
        print("Please enter your height as an integer.")

height = height / 100

weight_ok = False
while not weight_ok:
    try:
        weight = int(input("Enter your weight (kg): "))
        if 0 < weight < 301:
            weight_ok = True
        else:
            print("Please enter a valid weight between 1 and 300 kg.")
    except ValueError:
        print("Please enter your weight as an integer.")

bmi = weight / (height ** 2)
print(f"Your BMI is: {round(bmi, 3)}")

if bmi < 18:
    print("You have a thin body.")
elif 18 <= bmi <= 25:
    print("You have a normal body shape.")
elif 25 < bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
