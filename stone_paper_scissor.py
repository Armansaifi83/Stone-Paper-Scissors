import random 

print("=== Stone Paper Scissors Game ===")

chances = int(input("Enter number of chances: "))

user_score = 0
comp_score = 0

choices = ["stone", "paper", "scissor"]

for i in range(chances):
    print(f"\nChance {i+1}/{chances}")

    user_choice = input("Enter stone, paper, or scissor: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Chance skipped.")
        continue

    comp_choice = random.choice(choices)

    print("Computer chose:", comp_choice)

    # Determine winner of the round
    if user_choice == comp_choice:
        print("Round Draw!")

    elif (
        (user_choice == "stone" and comp_choice == "scissor") or
        (user_choice == "paper" and comp_choice == "stone") or
        (user_choice == "scissor" and comp_choice == "paper")
    ):
        print("You Win This Round!")
        user_score += 1

    else:
        print("Computer Wins This Round!")
        comp_score += 1

# Final Scores
print("\n=== Final Score ===")
print("User Score:", user_score)
print("Computer Score:", comp_score)
# Decide Overall Winner
if user_score > comp_score:
    print("Congratulations! You Won the Game.")
elif comp_score > user_score:
    print("Computer Won the Game.")
else:
    print("The Game is a Draw.")