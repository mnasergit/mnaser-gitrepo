a = "5/4"
b = "5/5"
a_parts = a.split("/")
b_parts = b.split("/")
a_numerator = int(a_parts[0])
a_denominator = int(a_parts[1])
b_numerator = int(b_parts[0])
b_denominator = int(b_parts[1])

list_numerator = [a_numerator, b_numerator]
list_denominator = [a_denominator, b_denominator]

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

lcm = find_lcm_of_list(list_denominator)

#print("LCM of", list_denominator, "is:", lcm)

a_numerator = int((lcm / a_denominator) * a_numerator)
b_numerator = int((lcm / b_denominator) * b_numerator)

if a_numerator == b_numerator:
    print(f"{a} equals to {b}")
elif a_numerator > b_numerator:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is less than {b}")