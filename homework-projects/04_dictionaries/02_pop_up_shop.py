# Problem Statement
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

def main():
    # Fruit prices per item
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0.0

    # Ask how many of each fruit the user wants
    for fruit in fruits:
        try:
            quantity = int(input(f"How many ({fruit}) do you want?: "))
        except ValueError:
            quantity = 0  # Treat invalid input as 0
        total_cost += fruits[fruit] * quantity

    print(f"\nYour total is ${total_cost:.2f}")


# Python boilerplate to run the main function
if __name__ == '__main__':
    main()
