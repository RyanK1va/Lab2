
weight = float(input("Enter yr weight(kg):"))
height = float(input("Enter yr height(m):"))
BMI = weight/(height * height)
print(f"BMI=",BMI)
if BMI < 18.5:
    print(f"Category: Underweight",BMI)
elif BMI < 24.9:
    print(f"Category: Normal")
elif BMI < 29.9:
    print(f"Category: Overweight")
else:
    print(f"Category: Obese")