def play_game(age):
    if age < 18:
        raise ValueError("Age must be 18 or above to play the game")
    else:
        print("Let's play the game!")


while True:
    try:
        user_age_str = input("Enter your age: ")
        user_age = int(user_age_str)

        if user_age < 18:
            raise ValueError("Age must be 18 or above to play the game")
        else:
            play_game(user_age)
            break  # Break the loop if the game can be played
    except ValueError as e:
        print(f"Error: {e}")
        print("Please enter a valid age.")
    except KeyboardInterrupt:
        print("\nUser interrupted the program.")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break
    finally:
        print("Game over. Thank you for playing!")
