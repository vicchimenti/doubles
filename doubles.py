import datetime


def validate_time(date_in):
    try:
        datetime.datetime.strptime(date_in, '%y-%m-%d')
    except ValueError:
        print('Invalid Date Format, enter format YY-MM-DD')
        return False
    print("You entered a valid date")
    return True


def get_user_input():
    # Option for User Input
    date_input = input("Enter any month and day in the format YY-MM-DD: ")
    return date_input


# Get Current Timestamp and Display Before Program Action
date_today = datetime.datetime.now()
print("Current Date/Time: ")
print(str(date_today))

# call get user input function
user_input = get_user_input()

# call validate time function
print(str(validate_time(user_input)))

# Get Updated Timestamp and Display After Program Action
date_today = datetime.datetime.now()
print("Current Date/Time: ")
print(str(date_today))
