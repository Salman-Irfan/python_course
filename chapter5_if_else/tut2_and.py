# Dummy user data
users = {
    "user1@example.com": "password123",
    "user2@example.com": "qwerty456",
    "user3@example.com": "letmein789",
}


# Login function

email = input("Enter your email: ")
password = input("Enter your password: ")

# Check if the email exists in the users dictionary
if email in users:
    # Check if the password matches the one stored for the email
    if users[email] == password:
        print("Login successful!")
    else:
        print("Incorrect password. Please try again.")
else:
    print("Email not found. Please try again.")
