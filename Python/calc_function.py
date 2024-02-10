#!C:\Users\abdullah.naser\AppData\Local\Programs\Python\Python312\python.exe
# Your Python script starts here

import sys

# Add Function #
def add(x,y):
    result = x + y
    return result

# Substract Function #
def sub(x,y):
    result = x - y
    return result

# Multiplication Function #
def mul(x,y):
    result = x * y
    return result

# Division Function #
def div(x,y):
    result = x / y
    return result

# Square Function #
def sqr(x,y):
    result = x ** y
    return result

# Math Operation Function #
def operations(x,y,operation):
    if operation == 1:
        print(f"Result of addition is: {add(x,y):.2f}")
    elif operation == 2:
        print(f"Result of substraction is: {sub(x,y):.2f}")
    elif operation == 3:
        print(f"Result of multiplication is: {mul(x,y):.2f}")
    elif operation == 4:
        print(f"Result of division is: {div(x,y):.2f}")
    elif operation == 5:
        print(f"Result of square is: {sqr(x,y):.2f}")

# Main Function #
def main():
    while True:
        print(" ")
        x = input(f"Enter your 'first' number: ")
        if x == "Q" or x == "q":
            sys.exit()
        try:
            x = float(x)
            break
        except:
            print("Enter a valid number. Or enter 'q' to quit.")
    while True:
        y = input(f"Enter your 'second' number: ")
        if y == "Q" or y == "q":
            sys.exit()
        try:
            y = float(y)
            break
        except:
            print("Enter a valid number. Or enter 'q' to quit.")

    print("*" * 49)
    print("1. Add         2. Substract     3. Multiplication")
    print("4. Division    5. Square                         ")
    print("*" * 49)

    while True:
        operation = input(f"Enter your preffered operation: ")

        if operation == "Q" or operation == "q":
            sys.exit()
        try:
            operation = int(operation)
            if operation >= 1 and operation <= 5:
                break
        except:
            print("Enter a valid 'integer' number listed above. Or enter 'q' to quit.")

    # Call operations() with the values returned from main()
    print(" ")
    operations(x, y, operation)

    print(" ")
    while True:
        cont = input(f"Do you want to continue (Y/N): ")
        if cont == "N" or cont == "n":
            sys.exit()
        if cont == "Y" or cont == "y":
            main()       

# Call main() to execute the code
if __name__ == "__main__":
    main()
