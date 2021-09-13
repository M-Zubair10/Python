# Part C:                         Finding the right amount to save away
#################

# Getting Inputs:
annual_salary = int(input("Enter Starting Annual Salary: "))
storage = annual_salary

# Initializing Variables:
total_cost = 1000000
raise_in_salary = 0.07
portion_down_payment = total_cost * 0.25
current_saving = 0
number_of_guesses = 0
low = 0
high = 1
guess = (low+high)/2

# Working:
while current_saving < portion_down_payment:
    for month in range(1 , 37):
        monthly_salary = annual_salary / 12
        current_saving += guess * monthly_salary + current_saving * 0.04/12
        if month % 6 == 0:
            annual_salary += annual_salary * raise_in_salary

# For Bisection Search
    if current_saving < portion_down_payment:
        current_saving = 0
        low = guess
    elif current_saving > portion_down_payment + 1000:
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
    print("Number of Guesses: ", number_of_guesses)
    print("It is not possible to pay the down payment in three years")
else:
    print("Best savings rate: ", guess)
    print("Steps in bisection search: ", number_of_guesses)
#                                  ______________________________
