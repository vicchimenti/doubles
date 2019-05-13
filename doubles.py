import datetime


def validate_time(date_in):
    try:
        datetime.datetime.strptime(date_in, '%y-%m-%d')
    except ValueError:
        print('Invalid Date Format, enter format YY-MM-DD')
        return False
    print("You entered a valid date")
    return True


# Get Current Timestamp and Display Before Program Action
date_today = datetime.datetime.now()
print("Current Date/Time: ")
print(str(date_today))

# Option for User Input
date_input = input("Enter any month and day in the format YY-MM-DD: ")
print(str(validate_time(date_input)))

# Get Current Timestamp and Display After Program Action
date_today = datetime.datetime.now()
print("Current Date/Time: ")
print(str(date_today))
