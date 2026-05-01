def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operator"


def main():
    print("=== Simple CLI Calculator ===")
    print("Operations: +  -  *  /")
    print("Type 'q' anytime to exit\n")

    while True:
        user_input = input("Enter first number: ")

        if user_input.lower() == 'q':
            print("Exiting calculator...")
            break

        try:
            num1 = float(user_input)
        except:
            print("Invalid input. Please enter a number.\n")
            continue

        operator = input("Enter operator (+, -, *, /): ")

        if operator.lower() == 'q':
            print("Exiting calculator...")
            break

        num2_input = input("Enter second number: ")

        if num2_input.lower() == 'q':
            print("Exiting calculator...")
            break

        try:
            num2 = float(num2_input)
        except:
            print("Invalid input. Please enter a number.\n")
            continue

        result = calculate(num1, num2, operator)

        print("Result:", result)
        print("-" * 30)


if __name__ == "__main__":
    main()