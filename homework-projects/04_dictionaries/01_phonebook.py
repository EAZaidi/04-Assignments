# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}
    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number
    return phonebook


def print_phonebook(phonebook):
    """
    Prints all the names and numbers in the phonebook.
    """
    print("\nPhonebook entries:")
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")


def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers by name.
    """
    print("\nLookup phase (press enter to stop):")
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# Python boilerplate to run the program
if __name__ == '__main__':
    main()