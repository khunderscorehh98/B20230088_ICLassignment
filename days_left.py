from datetime import datetime, timedelta

def day_counter(graduation_date, graduation_month, graduation_year):
    convertDate = datetime(graduation_year, graduation_month, graduation_date)
    x = datetime.today()

    # Exclude the final date by reducing one day from the total difference
    graduationLeft = convertDate - x - timedelta(days=1)

    # Initialize counters for working days and non-working days
    working_days = 0
    non_working_days = 0

    # Loop through each day between today and the day before graduation
    for i in range(graduationLeft.days):
        current_day = x + timedelta(days=i)
        if current_day.weekday() < 5:  # Monday to Friday are considered working days
            working_days += 1
        else:
            non_working_days += 1

    # Include the final date in the working day count if it's a working day
    if convertDate.weekday() < 5:
        working_days += 1

    return graduationLeft.days, working_days, non_working_days

graduation_date = int(input('Enter Graduation Date: '))
graduation_month = int(input('Enter Graduation Month: '))
graduation_year = int(input('Enter Graduation Year: '))

days_left, working_days, non_working_days = day_counter(graduation_date, graduation_month, graduation_year)

print(f"{days_left} days left until graduation, excluding the final date.")
print(f"Working days left: {working_days}")
print(f"Non-working days left: {non_working_days}")