# arithmetic_operations.py
# Objective: Define a function that performs basic arithmetic operations.

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs a basic arithmetic operation based on the operation parameter.
    
    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').
    
    Returns:
        float or str: The result of the operation or an error message for invalid cases.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation. Please choose add, subtract, multiply, or divide."
