# Problem Statement
# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

def main():
    # Countdown from 10 to 1
    for i in range(10, 0, -1):  # Start at 10, stop at 0 (not included), step -1
        print(i)
    print("Liftoff!")

if __name__ == '__main__':
    main()
