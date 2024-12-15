def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (potential issue)
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")