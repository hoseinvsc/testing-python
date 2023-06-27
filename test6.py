def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    i = sum(numbers)
    average = i / len(numbers)
    return average



numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print(" miyangiin;", average)