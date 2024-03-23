import random

num = [1, 2, 3, 4, 5, 6, 7, 8]

# Pick three random values from the list
random_values = random.sample(num, 3)

# Sort the random values in ascending order
ordered_values_ascendig = sorted(random_values)

# Sort the random values in descending order
ordered_values_descending = sorted(random_values, reverse=True)

# Convert the ascending and descending sorted lists to integers
min_number = int(''.join(map(str, ordered_values_ascendig)))
max_number = int(''.join(map(str, ordered_values_descending)))

# Calculate the difference between the maximum and minimum numbers
result_sub = max_number - min_number

print("Result of subtraction:", result_sub)

