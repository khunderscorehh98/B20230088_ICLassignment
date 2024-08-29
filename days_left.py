from datetime import datetime

def day_counter(graduation_date, graduation_month, graduation_year):
    convertDate = datetime(graduation_year, graduation_month, graduation_date)
    x = datetime.today()
    graduationLeft = convertDate - x 

    return graduationLeft.days

graduation_date = int(input('Enter Graduation Date: '))
graduation_month = int(input('Enter Graduation Month: '))
graduation_year = int(input('Enter Graduation Year: '))
days_left = day_counter(graduation_date, graduation_month, graduation_year)
print(f"{days_left} days left until graduation.")
