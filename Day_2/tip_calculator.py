print("Welcome to the Tip Calculator")
cost = float(input("Enter the cost of the bill "))
people = int(input("Enter the number of people "))
tip = float(input("Enter the tip percentage "))
tip = tip/100
tip = ((cost/people)*(1+tip))
tip = round(tip,2)
print(f"Each Person has to pay {tip}")