# Problem Statement
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

def main():
    # Ask the user for their favorite animal
    animal = input("What's your favorite animal? ")

    # Respond with the same favorite animal
    print(f"My favorite animal is also {animal}!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
