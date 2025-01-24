"""
This is a simple calculator script that performs basic arithmetic operations like
addition, subtraction, multiplication, and division. The user can continue to
perform operations or start a new calculation.
"""

from com.mateusdalcantara.resources.Logo import logo

def add(n1, n2):
    """
    Adds two numbers.

    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.

    Returns:
    float: The sum of n1 and n2.
    """
    return n1 + n2

def subtract(n1, n2):
    """
    Subtracts the second number from the first number.

    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.

    Returns:
    float: The result of n1 minus n2.
    """
    return n1 - n2

def multiply(n1, n2):
    """
    Multiplies two numbers.

    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.

    Returns:
    float: The product of n1 and n2.
    """
    return n1 * n2

def divide(n1, n2):
    """
    Divides the first number by the second number.

    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.

    Returns:
    float: The result of n1 divided by n2.

    Raises:
    ZeroDivisionError: If n2 is zero, since division by zero is not allowed.
    """
    if n2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return n1 / n2

# Dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    """
    Starts the calculator, allows the user to perform multiple arithmetic
    operations. The user can choose to accumulate the result or start a new calculation.
    """
    print(logo)
    should_accumulate = True
    num1 = float(input("First number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("Second number: "))

        # Perform the operation based on user input
        answer = operations[operations_symbol](num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")

        # Ask if the user wants to continue or start a new calculation
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()  # Recursively call calculator to start a new calculation

# Run the calculator function
calculator()

# Example usage of operations (commented out)
# print(operations["*"](4, 8))