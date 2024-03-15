# Define a dictionary representing user information
user = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "is_active": True,
    "height": 175.5,
    "address": {"street": "123 Main St", "city": "Anytown", "zipcode": "12345"},
    "skills": ["Python", "JavaScript", "SQL"],
    "friends": ("Alice", "Bob", "Charlie"),
    "preferences": None,
}

# Print the user dictionary
print(type(user))  # dict
print("User information:")
print(user)

# Accessing elements in the dictionary
print("\nAccessing elements:")
print("Name:", user["name"])
print("Age:", user["age"])
print("Email:", user["email"])
print("Is Active:", user["is_active"])
print("Height:", user["height"])
print("Address:", user["address"])
print("Skills:", user["skills"])
print("First friend:", user["friends"][0])
print("Preferences:", user["preferences"])
