shopping_cart = [
    {"id": 1, "item": "apples", "price": 15},
    {"id": 2, "item": "mangoes", "price": 20},
    {"id": 3, "item": "bananas", "price": 25},
    {"id": 4, "item": "oranges", "price": 30},
]

# initialize total cost
total_cost = 0

# calculate total cost
for item in shopping_cart:
    total_cost += item["price"]

print(f"Total cost of items in the shopping cart: {total_cost}")
