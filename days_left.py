from datetime import datetime, timedelta  # Import to handle date and time calculations

# Function to calculate total days, working days (Mon-Fri), and non-working days (Sat-Sun)
def calculate_days_to_graduation(grad_day, grad_month, grad_year):
    # Step 1: Convert the graduation date into a date object
    graduation_date = datetime(grad_year, grad_month, grad_day)

    # Step 2: Get today's date (current date)
    today_date = datetime.today()

    # Step 3: Calculate the difference in days between graduation day and today
    days_left = (graduation_date - today_date).days  # Total days until graduation

    # Step 4: Set counters for working and non-working days
    working_days = 0
    non_working_days = 0

    # Step 5: Loop through the range of days left until graduation
    for day in range(days_left):
        # Calculate each date one by one
        current_day = today_date + timedelta(days=day)
        
        # Step 6: Check if it's a working day (Mon-Fri) or non-working day (Sat-Sun)
        if current_day.weekday() < 5:  # Weekdays: Monday=0, Friday=4
            working_days += 1
        else:
            non_working_days += 1

    # Step 7: Include graduation day if it falls on a working day
    if graduation_date.weekday() < 5:
        working_days += 1

    # Return the results
    return days_left, working_days, non_working_days

# Input: Ask the user to enter their graduation date
grad_day = int(input("Enter the day you will graduate (1-31): "))
grad_month = int(input("Enter the month you will graduate (1-12): "))
grad_year = int(input("Enter the year you will graduate (e.g., 2024): "))

# Call the function to calculate the days remaining
days_left, working_days_left, non_working_days_left = calculate_days_to_graduation(grad_day, grad_month, grad_year)

# Output: Display the results to the user
print(f"Days left until graduation: {days_left} days")
print(f"Working days left: {working_days_left} days")
print(f"Non-working days left: {non_working_days_left} days")