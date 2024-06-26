import random

choices = ["rock", "paper", "scissors"]

x = random.choice(choices)
userchoice = input("please enter rock, paper, or scissors: ")
while userchoice == "":
    print("you didn't enter anything")
    userchoice = input("please enter rock, paper, or scissors: ")
if userchoice == x:
    print ("it is a tie")
elif userchoice =="rock" and x == "scissors":
    print("you win")
elif userchoice =="rock" and x =="paper":
    print("you lose")
elif userchoice =="paper" and x == "rock":
    print("you win")
elif userchoice =="paper" and x == "scissors":
    print("you lose")
elif userchoice =="scissors" and x == "rock":
    print("you lose")
elif userchoice =="scissors" and x == "paper":
    print("you win")
