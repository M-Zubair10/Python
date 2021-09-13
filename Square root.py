square_root: int = int(input("Enter Number:"))
Guess = 2
min = square_root - 0.0000002
max = square_root + 0.0000002
while Guess * Guess < min or Guess * Guess > max:
    Guess = (Guess + square_root / Guess) / 2
print('Square root of number is : ', Guess)


