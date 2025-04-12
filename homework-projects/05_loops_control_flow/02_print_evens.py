# Problem Statement
# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

# The first even number is 0:

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

def main():
    # Loop through the first 20 numbers (0 through 19)
    for i in range(20):
        print(i * 2)  # Multiply each index by 2 to get even numbers

# This line ensures main() is called when the script runs
if __name__ == '__main__':
    main()
