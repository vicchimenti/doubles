import datetime


# function for validating user input is a valid date in the requested format
def validate_time(date_in):
    try: datetime.datetime.strptime(date_in, '%y-%m-%d')
    except ValueError:
        print('Invalid Date Format, enter format YY-MM-DD')
        return False
    print("You entered a valid date")
    return True


# function for gathering user input
def get_user_input():
    # date_input = input("Enter any month and day in the format YY-MM-DD: ")
    # Stub user input instead
    date_input = stub_user_input()
    return date_input


# stub user input function and return a hard-coded valid date
def stub_user_input(): return "01-01-01"


# function for generating the current timestamp
def current_timestamp():
    date_today = datetime.datetime.now()
    print("Current Date/Time: ")
    return date_today


#   ***   main driver   ***   #
# Get Current Timestamp and Display Before Program Action
print(str(current_timestamp()))
# call get user input function
user_input = get_user_input()
# call validate time function
print(str(validate_time(user_input)))
# Get Updated Timestamp and Display After Program Action
print(str(current_timestamp()))
