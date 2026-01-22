import random
options=["rock","paper","scissor"]
computer_wins=0
user_wins =0
while True:
    user_choice = input("choose between, rock,paper ,sicissor, or q for quitting the game")
    if user_choice == "q":
        break
     #we take input from the user, if he says q, we just quit the loop
     #if user inputs some gibberish, we skip one beat of loop, and goes to next one using continue
    if user_choice not in options:
        continue
    # here 0 is rock , 1 is paper ,2 is scissor
    index = random.randint(0,2)
    #here random is a module(its simply means external file) we imported, it is a preinstalled in python, randint is a function of that module, we just use,. radint() to use that
    
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

