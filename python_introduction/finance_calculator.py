monthly_income = input("Enter your monthly income:")
monthly_expenses = input("Enter your total monthly expenses:")
monthly_savings = int(monthly_income) - int(monthly_expenses)
annual_interest = 0.05
Projected_savings = monthly_savings * 12 + (monthly_savings*12*0.05)
print("Your monthly savings are", "$"+str(int(monthly_savings)))
print("Projected savings after one year, with interest, is:", "$"+str(int(Projected_savings)))

