# Problem Statement
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def main():
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    quotient: int = dividend // divisor  
    remainder: int = dividend % divisor  
    
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


if __name__ == '__main__':
    main()
