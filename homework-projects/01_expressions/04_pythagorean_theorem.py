# Problem Statement
# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.

import math

def main():
    # Prompt the user for the lengths of the two perpendicular sides
    ab = float(input("Enter the length of side AB: "))
    ac = float(input("Enter the length of side AC: "))

    # Calculate the hypotenuse (BC) using the Pythagorean theorem
    bc = math.sqrt(ab ** 2 + ac ** 2)

    # Output the result
    print("The length of the hypotenuse (BC) is", bc)

# Required line to call the main() function
if __name__ == '__main__':
    main()
