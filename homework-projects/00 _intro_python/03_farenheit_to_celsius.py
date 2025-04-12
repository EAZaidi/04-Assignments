# Problem Statement
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

def main():
    # Prompt the user for temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Output the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
