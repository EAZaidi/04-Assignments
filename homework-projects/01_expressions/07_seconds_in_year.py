# Problem Statement
# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

# Useful constants
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

def main():
    # Calculate total seconds in a year
    seconds_per_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    # Print the result in a friendly sentence
    print("There are " + str(seconds_per_year) + " seconds in a year!")

# This line ensures main() runs when the script is executed
if __name__ == '__main__':
    main()
