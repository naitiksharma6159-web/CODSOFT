import random

def play_game():
    choices = ["rock", "paper", "scissors"]

    user_choice = input(f"Enter your choice ({', '.join(choices)}): ").strip().lower()
    while True:
        if user_choice not in choices:
            user_choice = input("Invalid choice. Please enter a valid choice: ").strip().lower()
        else:
            break

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

        
if __name__ == "__main__":
    play_game()
