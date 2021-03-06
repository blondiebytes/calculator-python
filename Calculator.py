def gather_inputs():
    operation = input("Please type in operation you would like to complete: +, -, *, or /")
    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))
    return operation, number_1, number_2

def run_operation(number_1,  number_2, operation):
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
        print('{} / {} = '.format(number_1, number_2), end = '')
        return number_1 / number_2
    else:
        raise Exception('This operator is invalid. Try running the program again.')

def main():
    print("Welcome")
    operation, number_1, number_2 = gather_inputs()
    print(run_operation(number_1, number_2, operation))

if __name__ == "__main__":
	main()