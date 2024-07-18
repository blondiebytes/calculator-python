def gather_inputs():
    """
    Gathers input from the user for the operation and numbers.
    Returns:
        tuple: operation (str), number_1 (int), number_2 (int)
    """
    # Gather operation and numbers from the user
    operation = input("Please type in operation you would like to complete: +, -, *, or /: ")
    try:
        number_1 = int(input('Please enter the first number: '))
        number_2 = int(input('Please enter the second number: '))
    except ValueError:
        raise ValueError("Please enter valid numbers.")
    return operation, number_1, number_2

def run_operation(number_1, number_2, operation):
    """
    Executes the given operation on the provided numbers.
    Args:
        number_1 (int): The first number.
        number_2 (int): The second number.
        operation (str): The operation to be performed (+, -, *, /).
    Returns:
        float: The result of the operation.
    Raises:
        Exception: If an invalid operator is provided.
        ZeroDivisionError: If division by zero is attempted.
    """
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2), end = '')
        return number_1 + number_2
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2), end = '')
        return number_1 - number_2
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2), end = '')
        return number_1 * number_2
    elif operation == '/':
        if number_2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        print('{} / {} = '.format(number_1, number_2), end = '')
        return number_1 / number_2
    else:
        raise Exception('This operator is invalid. Try running the program again.')

def main():
    """
    Main function to run the calculator program.
    """
    print("Welcome")
    operation, number_1, number_2 = gather_inputs()
    print(run_operation(number_1, number_2, operation))

if __name__ == "__main__":
    main()
