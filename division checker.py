# Main function
def main():
    number = float(input("Enter the number: "))                                         # Takes the user input for the number
    is_divisible = float(input(f"{number} divisible by? "))                             # Takes the user input for the divisible part
    result = convert(number, is_divisible)                                              # The convert function takes arguements and store a return value in the result variable

    if result is True:
        print(f"It is {result} that {number} is divisiable by {is_divisible}.")         # Prints this string if the result is True
    else:
        print(f"It is {result} that {number} is divisiable by {is_divisible}")          # Prints this string if the result is False


# Conversion function
def convert(x, n):
    if x % n == 0:
        return True                                                                     # Returns true if the modulus of x is equal to 0
    else:
        return False                                                                    # Returns false if the modulus of x is not equal to 0
    

main()                                                                                  # Calls the main function