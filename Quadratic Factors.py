# Home:
print("                                                        Find Quadratic factors!")
# Getting Inputs:
square_X = int(input("Enter Coefficient of x²: "))
normal_X = int(input("Enter Coefficient of x: "))
constant_term = int(input("Enter Coefficient of Constant: "))

# Variables:
rough = square_X * constant_term
second_factor = 1
first_factor = normal_X - second_factor
max_num = 1000
min_num = 1
chain = 10000000

# Working:
if square_X == 0:
    print("This is not Quadratic.As x² = 0,so it reduce to linear equation.")
else:
    while min_num < max_num:
        if first_factor*second_factor != rough:
            second_factor -= 1
            first_factor = normal_X - second_factor
        else:
            print(" ")
            print("First Factor is: ", first_factor)
            print("Second Factor is: ", second_factor)
            chain = first_factor
            print("")
            break
        min_num += 1

# Restoring Variables for second loop:
    second_factor = 1
    first_factor = normal_X - second_factor
    min_num = 1

    if chain != 10000000:
        print("")
    else:
        while min_num < max_num:
            if first_factor * second_factor != rough:
                second_factor += 1
                first_factor = normal_X - second_factor
            else:
                print(" ")
                print("First Factor is: ", first_factor)
                print("Second Factor is: ", second_factor)
                break
            min_num += 1
        if first_factor * second_factor != rough:
            print(" ")
            print("We are sorry.Its factors is not possible.")
            print("Try using quadratic formula for that equation.")