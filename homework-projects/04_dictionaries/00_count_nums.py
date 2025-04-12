# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

def get_user_numbers():
    """
    Ask the user to enter numbers until a blank line is given.
    Returns a list of those numbers (as integers).
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        user_numbers.append(int(user_input))
    return user_numbers


def count_nums(num_lst):
    """
    Takes a list of numbers and returns a dictionary where the keys are numbers
    and the values are the count of how many times they appear in the list.
    """
    num_dict = {}
    for num in num_lst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return num_dict


def print_counts(num_dict):
    """
    Prints how many times each number appears.
    """
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")


def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


if __name__ == '__main__':
    main()
