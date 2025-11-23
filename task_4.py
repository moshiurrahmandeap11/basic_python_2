# List Filtering

numbers = [10, 5, 23, 8, 100, 3, 44]

def filter_even_numbers(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers

def filter_odd_numbers(num_list):
    odd_numbers = [num for num in num_list if num % 2 != 0]
    return odd_numbers

def filter_greater_than_ten(num_list):
    greater_then_ten = [num for num in num_list if num > 10]
    return greater_then_ten

# Example usage
even_numbers = filter_even_numbers(numbers)
print(even_numbers)  # Output: [10, 8, 100,