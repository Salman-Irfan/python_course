# # Dummy user data
# users = {
#     "user1@example.com": "password123",
#     "user2@example.com": "qwerty456",
#     "user3@example.com": "letmein789",
# }


# # Login function

# email = input("Enter your email: ")
# password = input("Enter your password: ")

# # Check if the email exists in the users dictionary
# if email in users:
#     # Check if the password matches the one stored for the email
#     if users[email] == password:
#         print("Login successful!")
#     else:
#         print("Incorrect password. Please try again.")
# else:
#     print("Email not found. Please try again.")


# Dummy user data
users = {
    "user1@example.com": {"subscription": "premium"},
    "user2@example.com": {"subscription": "basic"},
    "admin@example.com": {"role": "admin"},
}


# Function to check access
def check_access(email):
    # Check if the user is an admin
    if email in users and "role" in users[email] and users[email]["role"] == "admin":
        return True
    # Check if the user has a premium subscription
    elif (
        email in users
        and "subscription" in users[email]
        and users[email]["subscription"] == "premium"
    ):
        return True
    else:
        return False


# Example usage
user_email = input("Enter your email: ")
if check_access(user_email):
    print("Access granted. You can access premium content.")
else:
    print("Access denied. You need a premium subscription or admin privileges.")
