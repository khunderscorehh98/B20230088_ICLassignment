def last_greater_backwd(lst, num):
    # Iterate over the list backwards using reversed index
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] >= num:
            return i
    # If no element is greater than or equal to num, return None
    return None

# Example usage:
lst = [1, 3, 5, 7, 9, 11]
num = 6

index = last_greater_backwd(lst, num)
print(f"The last index where the element is greater than or equal to {num} is: {index}")
