# Problem Statement
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Constant start of the sentence
SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "  # adjective noun verb

def main():
    # Get user input
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")

    # Combine and print the final sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# Required line to call the main function
if __name__ == '__main__':
    main()