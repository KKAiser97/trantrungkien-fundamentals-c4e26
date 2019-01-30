cm=float(input("Enter your height(cm): "))
h=cm/100
w=float(input("Enter your weight(kg): "))
bmi=w/(h*h)
print(bmi)
if bmi<16:
    print("Severely underweight")
elif bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal")
elif bmi<30:
    print("Overweigh")
else:
    print("Obese")