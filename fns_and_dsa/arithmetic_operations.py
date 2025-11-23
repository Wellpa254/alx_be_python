def perform_operation(num1, num2, operation):
    # Check the operation and perform the correct math
    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2

    else:
        # If user typed something wrong
        return "Error: Unknown operation"
