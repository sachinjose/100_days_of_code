weight,height = input("Enter the Weight and Height: ").split()
bmi = int(weight)/(float(height)**2)
if(bmi < 18.5):
	print(f"Your BMI is {bmi} ,You are Underweight")
elif(bmi < 25):
	print(f"Your BMI is {bmi} ,You are normal weight")
elif(bmi < 30):
	print(f"Your BMI is {bmi} ,You are overweight")
elif(bmi < 25):
	print(f"Your BMI is {bmi} ,You are obese")
else:
	print(f"Your BMI is {bmi} ,You are clinically obese")