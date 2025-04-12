# Problem Statement
# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements.

def main():
    # This for-loop starts at 0 and counts up to 19 (20 numbers total)
    for i in range(20):
        print(i * 2)  # Each 'i' multiplied by 2 gives the even number

if __name__ == '__main__':
    main()
