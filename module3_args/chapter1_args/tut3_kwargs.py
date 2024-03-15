def generate_profile(name, age, **kwargs):
    profile = {"name": name, "age": age}
    for key, value in kwargs.items():
        profile[key] = value
    return profile


# Generate a profile with additional information
user_profile = generate_profile(
    "John Doe", 30, city="New York", country="USA", occupation="Software Engineer"
)

print("User Profile:")
print(user_profile)
