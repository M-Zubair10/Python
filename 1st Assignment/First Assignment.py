# Question No 1: Write a program that does the following in order:
#                      1. Asks the user to enter a number “x”
#                      2. Asks the user to enter a number “y”
#                      3. Prints out number “x”, raised to the power “y”.
#                      4. Prints out the log (base 2) of “x”.
import numpy as np

first_num = int(input("Enter Number X: "))
second_num = int(input("Enter Number Y: "))
Power = first_num ** second_num
Logarithm = np.log2(first_num)
print("X**Y = " , Power)
print("log(x) = ", Logarithm)

# The End!
