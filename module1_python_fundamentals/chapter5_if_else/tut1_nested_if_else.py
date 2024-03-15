# Define the specific age thresholds
premium_age = 18
minimum_age = 12

# Get user's age
user_age = int(input("Enter your age: "))

# Check user's age and determine access level
if user_age >= premium_age:
    print("You can subscribe to the premium features of the game.")
elif user_age >= minimum_age:
    print("You can play the game without the premium package.")
else:
    print("Sorry, you are not old enough to play this game.")
