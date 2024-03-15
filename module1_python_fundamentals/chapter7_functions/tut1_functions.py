def calculate_total_cost(meal_cost, tax_rate, tip_rate):
    """
    Calculate the total cost of a meal including tax and tip.

    Args:
    - meal_cost (float): The cost of the meal before tax and tip.
    - tax_rate (float): The tax rate as a decimal (e.g., 0.07 for 7%).
    - tip_rate (float): The tip rate as a decimal (e.g., 0.15 for 15%).

    Returns:
    - total_cost (float): The total cost of the meal including tax and tip.
    """
    tax_amount = meal_cost * tax_rate
    tip_amount = meal_cost * tip_rate
    total_cost = meal_cost + tax_amount + tip_amount
    return total_cost


# Example usage
meal_cost = 50.0
tax_rate = 0.07  # 7%
tip_rate = 0.15  # 15%

total_cost = calculate_total_cost(meal_cost, tax_rate, tip_rate)
print("Total cost of the meal:", total_cost)
