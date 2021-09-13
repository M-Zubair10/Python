# Question No 1: House Hunting!

# Getting Inputs:
annual_salary = int(input("Enter Annual Salary: "))
portion_saved = float(input("Enter the percent of salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream house: "))

# Initializing Variables:
portion_down_payment = total_cost * 0.25
number_of_months = 0
current_saving = 0
monthly_salary = annual_salary / 12
# Working:

while current_saving <= portion_down_payment:
    monthly_return = current_saving * 0.04 / 12
    current_saving += portion_saved * monthly_salary + monthly_return
    number_of_months += 1

# Results:
print("Number of Years: ", number_of_months / 12)
#                                  ______________________________
