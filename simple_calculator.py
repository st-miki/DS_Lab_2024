results = []

while True:
    
    print("\nEnter two numbers and an operator (+, -, *, /) or 'q' to quit.")
    num1 = input("Enter the first number: ")
    
    if num1.lower() == 'q':  
        break
    
    num2 = input("Enter the second number: ")
    operator = input("Enter an operator (+, -, *, /): ")
    
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Cannot divide by zero!")
            continue
        result = num1 / num2
    else:
        print("Invalid operator! Please enter one of +, -, *, or /.")
        continue

    
    results.append(result)
    print(f"Result: {result}")


print("\nAll results:", results)
