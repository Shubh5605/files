#User Input: Prompt the user to choose rock, paper, or scissors.
#Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
#Game Logic: Determine the winner based on the user's choice and the computer's choice.
#Rock beats scissors, scissors beat paper, and paper beats rock.
#Display Result: Show the user's choice and the computer's choice.
#Display the result, whether the user wins, loses, or it's a tie.
#Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
#Play Again: Ask the user if they want to play another round.
#User Interface: Design a user-friendly interface with clear instructions and feedback.
import random
def play_game():
    choices = ["rock", "paper", "scissors"]

    while True:
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
        else:
            result = "Computer wins!"

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_game()
