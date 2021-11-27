#We import the modules that we need!
import sys
import time
import random

#We check if the player wants to play
print("Wecome to rock paper scsors. Wanna play? (put y o n)")
play_confirm = input()
if play_confirm == "n":
    sys.exit

#We load
print("Thanks for your response!")
time.sleep(2)
print("prepering algorithim")
time.sleep(1.5)
print("loading recources")
time.sleep(1)
print("Are you ready?")
#Player choice
print("Choose your wepon")
print("r rock, p paper, s siccors")
player_choice = False

#While true loop
while True: 
    player_choice = input()
    if player_choice!="r" and player_choice!="p" and player_choice!="s":
        print("error, letter not corresponding!")
        break

    print("Ok, the algorithim is choosing his wepon")
    time.sleep(5)

    #computer algorithim
    computer = random.randint(0,2)
    if computer==0:
        computer = "r"
    elif computer== 1:
        computer = "p"
    elif computer == 2:
        computer = "s"
    
    if player_choice == computer:
        print("Darw")
        print("Thanks for playing")
        break
    elif player_choice =="r" and computer=="s" or player_choice=="s" and computer=="p" or player_choice=="p" and computer=="r":
        print("You won!")
        print("Thanks for playing!")
        break
    else:
        print("The computer won, it will be for next time!")
        print("Thanks for playing!")
        break
    
print("exiting program!")

time.sleep(1)
