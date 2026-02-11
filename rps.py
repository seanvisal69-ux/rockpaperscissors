import random

choice = ["rock", "paper", "scissors"]
computerScore = 0
userScore = 0
winscore = 5

while computerScore < winscore and userScore < winscore:
    computer = random.choice(choice)
    user = input("Enter rock, paper, or scissors: ").lower()

    if user not in choice:
        print("Invalid choice! Please choose rock, paper, or scissors.")
    else:
        print("Computer chose:", computer)

        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):  
            userScore += 1
            print("You win this round! 🎉")
        else:
            computerScore += 1
            print("Computer wins this round! 😢")
        print(f"Current Score - You: {userScore}, Computer: {computerScore}\n")
if userScore == winscore:
    print("Congratulations! You won the game! 🎉")
else:    print("Computer won the game! Better luck next time! 😢")
            
   
    
