def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

# Example with error handling
try:
    my_numbers = [1, 2, 'a', 4, 5]  # Include non-numeric type
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")
