# First project power learn program module Python programming
# simple calculator program 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")  
if choice == '1':
    add = a + b
    print(f"{a} + {b} = {add}")
elif choice == '2':
    subtract = a - b
    print(f"{a} - {b} = {subtract}")
elif choice == '3':
    multiply = a * b
    print(f"{a} * {b} = {multiply}")
elif choice == '4':
    if b != 0:
        divide = a / b
        print(f"{a} / {b} = {divide}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input. Please select a valid operation (1/2/3/4).")
# End of calculator.py