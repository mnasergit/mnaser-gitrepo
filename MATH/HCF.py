list = [10, 30]
hcf = 1

# Find common factors of all numbers
for i in range(2, min(list) + 1):
    if all(num % i == 0 for num in list):
        hcf = i

print("HCF of", list, "is:", hcf)

########################################

def find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (a * b) // find_hcf(a, b)

def find_lcm_of_list(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = find_lcm(lcm, num)
    return lcm

lcm = find_lcm_of_list(list)

print("LCM of", list, "is:", lcm)