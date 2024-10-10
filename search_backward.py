# Function to find the last index where a number is greater than or equal to the target
def find_last_greater_or_equal(numbers_list, target_number):
    last_index = -1  # Start with -1 to show we haven't found anything yet

    # Go through the list one by one using a for loop
    for i in range(len(numbers_list)):  # i is the index of each element in the list
        if numbers_list[i] >= target_number:  # If the current number is bigger or equal to target_number
            last_index = i  # Remember the index of this number

    # If we found a number, return its index, otherwise return None
    if last_index != -1:
        return last_index
    else:
        return None  # Return None if no match was found

# Input section: ask the user to give a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")  
# Split the input string by spaces and convert each part into an integer to form a list of numbers
numbers_list = [int(number) for number in user_input.split()]  

# Ask the user to give a target number to compare with the list
target_number = int(input("Enter the number to compare with the list: "))

# Call the function to get the last index where a number is greater or equal to the target
index_result = find_last_greater_or_equal(numbers_list, target_number)

# Show the result to the user
if index_result is not None:
    print(f"The last index where a number is greater than or equal to {target_number} is: {index_result}")
else:
    print(f"No number in the list is greater than or equal to {target_number}.")
