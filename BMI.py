height=float(input("Enter Height in Meter="))
weight=float(input("Enter Weight in Kg="))
bmi=round(weight/height**2)
if bmi<18.5:
  print(f"You are Underweight {bmi}.")
elif bmi<25.5:
  print(f"You are Normal {bmi}.")
elif bmi<30.5:
  print(f"You are overweight {bmi}.")
elif bmi<35.5:
  print(f"You are obese {bmi} .")
else:
  print(f"You are clinically obese {bmi} .")
 