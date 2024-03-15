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

# Looping over the dictionary using a for loop
print("Looping over the dictionary:")
for key in user:
    print(f"Key: {key}, Value: {user[key]}")

# Checking for the existence of keys using the in keyword
print("\nChecking for key existence:")
print("Is 'email' in user dictionary?", "email" in user)
print("Is 'phone' in user dictionary?", "phone" in user)

# Accessing dictionary values
print("\nAccessing dictionary values:")
print("Name:", user["name"])
print("Age:", user["age"])
print("Skills:", user["skills"])
