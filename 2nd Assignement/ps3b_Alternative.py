# Part C:                         Finding the right amount to save away
#################

# Home
print(f"\n {' '*50} Finding the right amount to save away!\n")
# Getting Inputs:
annual_salary = int(input("Enter Starting Annual Salary: "))
total_cost = int(input("Enter the Cost of your Dream House: "))
raise_in_salary = int(input("Enter semi-annual raise in salary in %: ")) * 0.01
number_of_months = float(input("Enter number of years: ")) * 12 + 1
invest = input("You want to invest your money;Yes or No: ")

# Initializing Variables:
storage = annual_salary
portion_down_payment = total_cost
current_saving = 0
number_of_guesses = 0
low = 0
high = 1
guess = (low+high)/2

# Working:
while current_saving < portion_down_payment:
    for month in range(1 , number_of_months):
        monthly_salary = annual_salary / 12
        current_saving += guess * monthly_salary
        if invest == "yes" or invest == "Yes":
            current_saving += current_saving * 0.04/12
        if month % 6 == 0:
            annual_salary += annual_salary * raise_in_salary

# For Bisection Search
    if current_saving < portion_down_payment:
        current_saving = 0
        low = guess
    elif current_saving > portion_down_payment + 100:
        current_saving = 0
        high = guess
    if number_of_guesses == 100:
        break

# Re-initializing Variables:
    annual_salary = storage
    guess = (low+high)/2
    number_of_guesses +=1

# Results:
if number_of_guesses == 100:
    print("")
    print("It is not possible to pay the down payment in three years")
else:
    print(" ")
    print("Best savings rate to purchase your house: ", guess)
    print("Steps in bisection search: ", number_of_guesses)
#                                  ______________________________
