# Read two numbers from the user
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

# Show menu
print("\nChoose an operation: ")
print("1. Add")
print("2. Substract")
print("3. Multiple")
print("4. Divide")

# Read Choice
choice=int(input("Enter the choice (1-4): "))

# Perform the operation based on the choice
if choice == 1:
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == 2:
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif choice == 3:
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice == 4:
    if num2 == 0:
        print("Divide by Zero Error")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
else:
    print("Invalid Choice")