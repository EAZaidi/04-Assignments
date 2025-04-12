# Problem Statement

# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.
def main():
    anton : int = 21
    beth : int = anton + 6
    chen : int = beth + 20
    drew : int = chen + anton
    ethan : int = chen

    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
