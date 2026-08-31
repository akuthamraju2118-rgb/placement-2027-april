import random

"""
 1 for rock
-1 for paper
0 for scissors
"""

# Initialize scores before starting the game loop
user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors!")
print("Type 'q' at any time to quit the game.\n")

# Main game loop
while True:
    # 1. Computer randomly chooses a value
    computer = random.choice([-1, 0, 1])

    # 2. Get user input and clean it up
    youstr = input("Enter your choice (r, p, s) or 'q' to quit: ").lower().strip()

    # 3. Check if the user wants to quit
    if youstr == 'q':
        print("\n--- Final Game Summary ---")
        print(f"Your Final Score: {user_score}")
        print(f"Computer's Final Score: {computer_score}")
        if user_score > computer_score:
            print("🏆 Congratulations! You won the entire match!")
        elif user_score < computer_score:
            print("💻 The computer wins this time. Better luck next time!")
        else:
            print("🤝 It's an overall draw!")
        print("Thanks for playing!")
        break  # Exits the loop and stops the program

    # 4. Dictionaries mapping inputs to choices
    youDict = {"r": 1, "p": -1, "s": 0}
    reverseDict = {1: "rock", -1: "paper", 0: "scissors"}

    # 5. Check if the user's input is valid
    if youstr not in youDict:
        print("❌ Invalid choice! Please enter 'r', 'p', 's', or 'q'.\n")
        continue  # Skips the rest of the loop and asks for input again

    # 6. Look up the integer value safely using the string key directly
    you = youDict[youstr]

    # Print choices
    print(f"\nYou chose: {reverseDict[you]}")
    print(f"Computer chose: {reverseDict[computer]}")

    # 7. Game Logic & Score Updating
    if computer == you:
        print("Its a draw!")
    else:
        if computer == -1 and you == 1:
            print("You lose!")
            computer_score += 1
        elif computer == -1 and you == 0:
            print("You win!")
            user_score += 1
        elif computer == 1 and you == 0:
            print("You lose!")
            computer_score += 1
        elif computer == 1 and you == -1:
            print("You win!")
            user_score += 1
        elif computer == 0 and you == -1:
            print("You lose!")
            computer_score += 1
        elif computer == 0 and you == 1:
            print("You win!")
            user_score += 1
        else:
            print("Something went wrong")

    # 8. Print current score standings
    print(f"👉 Current Score -> You: {user_score} | Computer: {computer_score}\n")
    print("-" * 30)
