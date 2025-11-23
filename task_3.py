# Exception Handling

def divide_numbers_function(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    

# Example usage
print(int(divide_numbers_function(10, 0)))