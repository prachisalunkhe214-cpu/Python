basic=float(input("Enter the basic salary:"))
da = float(input("Enter Dearness Allowance (DA): "))
hra = float(input("Enter House Rent Allowance (HRA): "))

# Calculate gross salary
gross_salary = basic + da + hra

# Display result
print("Gross Salary =", gross_salary)
