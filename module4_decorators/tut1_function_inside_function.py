# Suppose you are building a web application and you need to handle user authentication. You can create a function login_user(username, password) that checks if the provided username and password are valid. Additionally, you can have a function get_user_role(username) that retrieves the role of the user from a database. Here's how you can use a function inside another function for this scenario:


def authenticate_user(username, password):
    def check_credentials(username, password):
        # Logic to check if the username and password are valid
        return True  # Placeholder logic

    if check_credentials(username, password):
        role = get_user_role(username)
        return f"Welcome, {username}! Your role is {role}"
    else:
        return "Invalid credentials"


def get_user_role(username):
    # Logic to retrieve user role from database
    return "Admin"  # Placeholder logic


# Usage example
print(authenticate_user("john_doe", "password123"))
