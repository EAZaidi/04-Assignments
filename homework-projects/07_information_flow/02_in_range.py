# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n: int, low: int, high: int) -> bool:
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    return low <= n <= high  # More concise way to write the condition


def main():
    n = int(input("Enter a number to check: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    if in_range(n, low, high):
        print(f"{n} is in the range {low} to {high}.")
    else:
        print(f"{n} is NOT in the range {low} to {high}.")


# Required to call main
if __name__ == '__main__':
    main()
