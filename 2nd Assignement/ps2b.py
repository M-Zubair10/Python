#                                 Question No 2: Saving, with a raise!

# Getting Inputs:
annual_salary = int(input("Enter Starting Annual Salary: "))
portion_saved = float(input("Enter the percent of salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream house: "))
raise_in_salary = float(input("Enter semi-annual salary raise, as a decimal: "))

# Initializing Variables:
portion_down_payment = total_cost * 0.25
number_of_months = 0
current_saving = 0
# Working:

while current_saving < portion_down_payment:
    current_saving += portion_saved * annual_salary / 12 + current_saving * 0.04 / 12
    number_of_months += 1

    if number_of_months % 6 == 0:
        annual_salary += annual_salary * raise_in_salary

# Results:
print("Number of months: ", number_of_months)
#                                  ______________________________

