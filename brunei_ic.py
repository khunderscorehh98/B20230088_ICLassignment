import random  # Import the random module to generate random numbers

# Function to generate Brunei IC based on the user's nationality
def generate_ic(nationality):
    # Step 1: Set up the IC prefix based on nationality
    if nationality == '1':  # Local Bruneian
        ic_prefix = '00'  # Fixed value '00' for simplicity
    elif nationality == '2':  # Permanent Resident Bruneian
        ic_prefix = '03'
    elif nationality == '3':  # Other
        ic_prefix = '51'
    else:
        ic_prefix = ''  # Leave blank if the input is invalid

    # Step 2: Generate the remaining 6 digits for the IC number
    # Random number between 0 and 999999, and then make sure it's 6 digits long
    remaining_digits = random.randint(0, 999999)
    remaining_digits = str(remaining_digits).zfill(6)  # Add leading zeros if necessary

    # Step 3: Return the full IC number in "prefix-remaining_digits" format
    return ic_prefix + '-' + remaining_digits

# Function to replace each character of the password with 'x'
def mask_password(password):
    masked = ''
    for char in password:  # Loop through each character in the password
        masked += 'x'      # Replace every character with 'x'
    return masked

# Main part of the program
# Step 1: Get user inputs
student_name = input("Enter your name: ")
print("Select your nationality:")
print("1. Local Bruneian")
print("2. Permanent Resident Bruneian")
print("3. Other")
nationality = input("Enter the number (1, 2, or 3) that matches your nationality: ")

user_id = input("Create your User ID: ")
password = input("Create your password: ")

# Step 2: Generate the IC number based on nationality
ic_number = generate_ic(nationality)

# Step 3: Mask the password by replacing it with 'x'
masked_password = mask_password(password)

# Step 4: Display the results
print("\n--- Registration Details ---")
print("Student Name:", student_name)

# Show nationality based on the input
if nationality == '1':
    print("Nationality: Local Bruneian")
elif nationality == '2':
    print("Nationality: Permanent Resident Bruneian")
elif nationality == '3':
    print("Nationality: Other")
else:
    print("Invalid nationality choice!")

# Display user ID, IC, and masked password
print("User ID:", user_id)
print("Generated Brunei IC:", ic_number)
print("Masked Password:", masked_password)
