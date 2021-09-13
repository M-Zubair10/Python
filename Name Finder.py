actual_name = "Muhammad"
name = input("What is your name: ")
for char1 in actual_name:
    for char2 in name:
        if char2 == char1:
            break

