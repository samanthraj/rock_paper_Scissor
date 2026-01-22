import random
options=["rock","paper","scissor"]
computer_wins=0
user_wins =0
while True:
    user_choice = input("choose between, rock,paper ,sicissor, or q for quitting the game")
    if user_choice == "q":
        break
    if user_choice not in options:
        continue

    index = random.randint(0,2)
    computer_choice = options[index]

    if user_choice =="rock" and computer_choice =="scissor":
        print("You win")
        user_wins+=1
        continue
    elif user_choice =="paper" and computer_choice =="rock":
        print("You win")
        user_wins+=1
        continue
    elif user_choice =="scissor" and computer_choice == "paper":
        print("You win")
        user_wins+=1
        continue
    else:
        print("You Lose")
        computer_wins+=1
        continue


print("game is over")
print("scores.....")
print("User Wins:  ",user_wins)
print("Computer Wins:  ",computer_wins)
print("Good bye")
