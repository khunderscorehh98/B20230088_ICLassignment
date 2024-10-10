# Function to find the best number of rented units for maximum profit
def find_optimal_rent():
    # Step 1: Ask the user for necessary inputs
    total_units = int(input("Enter the total number of units: "))
    base_rent = float(input("Enter the rent when all units are occupied: "))
    rent_increase = float(input("Enter the rent increase for each vacant unit: "))
    maintenance_cost = float(input("Enter the maintenance cost per rented unit: "))

    # Step 2: Initialize variables to keep track of the best result
    best_profit = None  # This will store the highest profit we calculate
    best_rented_units = 0  # This will store the number of rented units for max profit

    # Step 3: Loop through each possible number of rented units
    for rented_units in range(total_units + 1):
        # Calculate the number of vacant units
        vacant_units = total_units - rented_units

        # Step 4: Calculate the current rent per rented unit
        current_rent = base_rent + (vacant_units * rent_increase)

        # Step 5: Calculate the profit for this number of rented units
        current_profit = (rented_units * current_rent) - (rented_units * maintenance_cost)

        # Step 6: Check if this is the best profit we've found so far
        if best_profit is None or current_profit > best_profit:
            best_profit = current_profit
            best_rented_units = rented_units

    # Step 7: Output the best result to the user
    print(f"To maximize profit, rent out {best_rented_units} units.")
    print(f"The maximum profit is: ${best_profit:.2f}")

# Step 8: Run the function to start the program
find_optimal_rent()