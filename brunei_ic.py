import random

def brunei_ic(nationality):
    ic_prefix = ''
    if nationality == '1':  # Local Bruneian
        ic_prefix = random.choice(['00', '01'])
    elif nationality == '2':  # Permanent Resident Bruneian
        ic_prefix = '03'
    elif nationality == '3':  # Other
        ic_prefix = '51'
    
    # Generate the remaining 6 digits of the IC number
    remaining_digits = str(random.randint(0, 999999)).zfill(6)
    
    return f"{ic_prefix}-{remaining_digits}"

def replace_password(password):
    return ''.join('x' for _ in password)

# Inputs
student_name = input('Please enter student name: ')
nationality = input('Please enter student nationality: \n1. Local Bruneian\n2. Permanent Resident Bruneian\n3. Other\nSelect your nationality (1, 2, 3): ')
user_id = input('Create your User ID: ')
password = input('Create your Password: ')

# Generate Brunei IC
ic_number = brunei_ic(nationality)

# Replace password with 'x'
masked_password = replace_password(password)

# Output
print(f"Student Name: {student_name}")
print(f"Nationality: {'Local Bruneian' if nationality == '1' else 'Permanent Resident Bruneian' if nationality == '2' else 'Other'}")
print(f"User ID: {user_id}")
print(f"Generated Brunei IC: {ic_number}")
print(f"Masked Password: {masked_password}")
