"""
Write a Python program that can simulate a simple calculator, using
the console as the exclusive input and output device. That is,
each input to the calculator, be it a number, like 12.34 or 1034,
or an operator, like + or =, can be done on a separate line. After
each such input, you should output to the Python console what would
be displayed on your calculator.
"""


def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2

    elif operation == "-":
        return num1 - num2

    elif operation == "*":
        return num1 * num2

    elif operation == "/":
        return num1 / num2

    elif operation == "**":
        return num1 ** num2

    else:
        return None


def main():
    while True:
        num1 = float(input("Enter number 1: "))
        operation = input("Enter operation (+, -, *, /, **): ")
        num2 = float(input("Enter number 2: "))

        output = calculate(num1, num2, operation)

        if output is None:
            print("Invalid operation!")
            continue

        elif output.is_integer():
            print(int(output))

        else:
            print(output)


if __name__ == "__main__":
    main()
