weight=float(input("enter your weight"))
height=float(input("enter your height"))
BMI =weight/(height**2)
if BMI>=18.5 and BMI<=24.9:
    print("normal weight")
elif BMI>=25.0 and BMI<=29.9:
    print("over weight")
elif BMI>=30.0 and BMI<=34.9:
    print("Obesty class 1")
elif BMI>=35.0 and BMI<=39.9:
    print("obesty class 2")
elif BMI>=40.0 and BMI<=49.9:
    print("obesty class 3")
else:
    print("invalid...")