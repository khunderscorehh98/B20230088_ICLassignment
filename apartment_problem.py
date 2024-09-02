def calculate_max_profit():
    # Prompt the user for input values
    N = int(input("Enter the total number of units: "))
    R = float(input("Enter the rent to occupy all the units: "))
    I = float(input("Enter the increase in rent that results in a vacant unit: "))
    M = float(input("Enter the maintenance cost per rented unit: "))
    
    max_profit = 0
    optimal_units = 0
    
    # Iterate through the possible number of vacant units (k)
    for k in range(N):
        occupied_units = N - k
        rent_per_unit = R + k * I
        profit = (occupied_units * rent_per_unit) - (occupied_units * M)
        
        if profit > max_profit:
            max_profit = profit
            optimal_units = occupied_units
    
    # Output the result
    print(f"The number of units to rent to maximize profit is: {optimal_units}")
    print(f"The maximum profit is: ${max_profit:.2f}")

# Call the function to execute the program
calculate_max_profit()