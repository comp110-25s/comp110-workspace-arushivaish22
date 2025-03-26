"""This is my wordle coding exercise!"""

__author__ = "730579218"


def contains_char(word: str, char: str) -> bool:
    """Tells you if the character is in the word."""
    assert len(char) == 1, f"len('{char}') is not 1"
    position: int = 0
    while position < len(
        word
    ):  # Iterating while loop that loops over each character in the word
        if word[position] == char:
            return True  # Return True if the character is found in word
        position = position + 1  # Move to next character in word

    return False  # Return False if the character is not found


def emojified(guess: str, secret: str) -> str:
    """Returns an emoji representing the accuracy of the guess."""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    # Colored box emojis
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    result: str = ""
    index: int = 0

    while index < len(
        guess
    ):  # Iterating while loop that loops over each character in the guess
        if (
            guess[index] == secret[index]
        ):  # If chatacter matches the secret at the same position
            result += GREEN_BOX  # Add a green box emoji
        elif contains_char(
            word=secret, char=guess[index]
        ):  # If chracter is in the secret but not at that position
            result += YELLOW_BOX  # Add a yellow box emoji
        else:  # If character is not in the secret
            result += WHITE_BOX  # Add a white box emoji
        index = index + 1  # Move on to the next character in the guess

    return result  # Return the feedback sting of emojis


def input_guess(expected_length: int) -> str:
    """Gets user to input a guess of the given length."""
    guess_word = input(f"Enter a {expected_length} character word: ")
    while (
        len(guess_word) != expected_length
    ):  # Keep asking for a new guess until the guess length matches expected length
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess_word  # Return the valid guess once of the expected length


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns_left: int = 6  # Maximum number of turns is 6
    turn_number: int = 1  # Start counting turns at 1
    correct_guess: bool = False  # Track correctness of guess

    while (
        turns_left > 0 and not correct_guess
    ):  # While loop continues when turns are left and guess is incorrect
        print(f"=== Turn {turn_number}/6 ===")  # Print current turn number

        guess = input_guess(len(secret))  # User inputs a guess of correct length
        feedback = emojified(guess, secret)  # Get feedback string of emojis
        print(feedback)  # Display emoji feedback
        if guess == secret:  # If guess matches secret word
            correct_guess = True  # Set the correctness track to True
            print(
                f"You won in {turn_number}/6 turns!"
            )  # Congratulate user and return number of turns it took
        else:
            turns_left = turns_left - 1  # Reduce number of turns left by 1
            turn_number = turn_number + 1  # Increase current term number by 1
            if turns_left == 0:
                print(
                    f"X/6 - Sorry, try again tomorrow!"
                )  # User is out of turns so tell them to return tomorrow


if __name__ == "__main__":
    main(secret="codes")
