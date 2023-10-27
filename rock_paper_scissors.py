import random


user_action = input("Enter a choice of rock, paper and scissors: ")

actions = ["rock, paper, scissors"]

computer_act = random.choice(actions)

if user_action == computer_act:
    print("both players selected", actions, "it's a tie!")

elif user_action == "rock":
    if computer_act == "scissors":
        print("Rock smashed scissors! you won!")
    else:
        print("Rock got wrapped by paper! you lost...")

elif user_action == "scissors":
    if computer_act == "paper":
        print("Scissors cut paper! you won!")
    else:
        print("scissors got broken by rock! you lost...")

elif user_action == "paper":
    if computer_act == "rock":
        print("Paper wraped rock! you won!")
    else:
        print("Paper got cut by scissors! you lost...")

