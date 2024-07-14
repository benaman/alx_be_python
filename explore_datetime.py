# Import necessary components from datetime module
from datetime import datetime

# Function to display current date and time
def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print formatted date and time
    print(f"Current date and time: {formatted_date}")

# Call the function to display current date and time
display_current_datetime()

# import necessary components from datetime module
from datetime import datetime, timedelta

# function to calculate future date
def calculate_future_date():
    # prompt user for number of days
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    # get current date
    current_date = datetime.now()

    # calculate future date
    future_date = current_date + timedelta(days=number_of_days)

    # format future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # print future date
    print(f"Future date: {formatted_future_date}")

# call the function to calculate future date
calculate_future_date()

