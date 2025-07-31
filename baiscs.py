def basic_calculator():
    """A simple calculator that performs basic arithmetic operations.
    Supports addition, subtraction, multiplication, and division.
    Handles errors for invalid inputs and division by zero."""
    
    print("Basic Calculator Program")
    print("------------------------")
    
    try:
        # Getting  user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ").strip()
        
        # Perform calculation based on user input
        result = None
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation! Please choose +, -, *, or /")
        
        # Display result
        print(f"{num1} {operation} {num2} = {result}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    basic_calculator()