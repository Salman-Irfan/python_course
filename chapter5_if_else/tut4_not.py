# Dummy user data
user_data = {"name": "Alice", "age": 25, "agree_to_terms": False}

# Check if the user has agreed to the terms and conditions
if not user_data["agree_to_terms"]:
    print(
        f"{user_data['name']}, you must agree to the terms and conditions to proceed."
    )
else:
    print(f"Welcome, {user_data['name']}! You have agreed to the terms and conditions.")


name = "salman"

if "a" in name:
    print("a is present in name")
else:
    print("a is not present in name")
