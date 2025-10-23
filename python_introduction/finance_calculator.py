# Prompt the user for their financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings (including 5% interest)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the results
print("Your monthly savings are:", monthly_savings)
print("Your projected savings after one year (with 5% interest) are:", projected_savings)