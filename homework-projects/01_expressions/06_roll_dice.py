# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.

"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

# Import the random library to simulate dice rolls
import random

# Number of sides on each die
NUM_SIDES = 6

def main():
    # Optional: set a random seed for consistent results during testing
    # random.seed(1)

    # Roll each die
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)

    # Calculate total
    total = die1 + die2

    # Display results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()
