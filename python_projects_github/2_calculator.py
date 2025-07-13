choice = input("Enter your choice (sum, subtract, division, multiplication): ")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if choice == "sum":
    result = number1 + number2
    print("Result:", result)

elif choice == "subtract":
    result = number1 - number2
    print("Result:", result)

elif choice == "multiplication":
    result = number1 * number2
    print("Result:", result)

elif choice == "divison":
    if number2 == 0:
        print("Can't divide by 0!")
    else:
        result = number1 / number2
        print("Result:", result)

else:
    print("Invalid selection!")

if 'result' in locals():
    print("Result:", result)
