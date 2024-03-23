# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of all numbers in the list
total_sum = sum(numbers)

# Determine the total number of elements in the list
count = len(numbers)

# Calculate the average
average = total_sum / count

print("Average of the numbers:", average)

###################################################

sorted_numbers = sorted(numbers)

# Calculate the index of the middle element
middle_index = count // 2

if count % 2 == 1:
    # If the list has odd number of elements, the median is the middle element
    median = sorted_numbers[middle_index]
else:
    # If the list has even number of elements, the median is the average of the two middle elements
    median = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2

print("Median of the numbers:", median)