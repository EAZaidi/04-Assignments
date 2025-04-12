# Problem Statement
# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

MINIMUM_HEIGHT: int = 50  # Minimum height requirement to ride

def main():
    height_input = input("How tall are you? ")
    if height_input:  # Checks if input is not empty
        height = float(height_input)
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

# Required line to call main when script is executed
if __name__ == '__main__':
    main()
