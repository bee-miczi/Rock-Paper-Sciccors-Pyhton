#importiamo i moduli che neccessitiamo
import sys
import time
import random

#Confernmzione che vuoi giocare
print("Benvenuto a morra cinese. Vuoi giocare? (immetti y o n)")
play_confirm = input()
if play_confirm == "n":
    sys.exit

#Prepariamo l'algoritmo
print("Grazie per la tua risposta")
time.sleep(2)
print("prepering algorithim")
time.sleep(1.5)
print("loading recources")
time.sleep(1)
print("Sei pronto?")
#facciamo scegliere l'arma
print("Scegli la tua arma")
print("s sasso, c carta, f forbice")
player_choice = False

#while loop
while True: 
    player_choice = input()
    #controlliamo l'arma se è guista
    if player_choice!="f" and player_choice!="c" and player_choice!="s":
        print("error, letter not corresponding!")
        break

    #facciamo scegliere l'arma al algoritmo
    print("Ok l'algoritmo sta scegliendo la sua arma")
    time.sleep(5)

    #computer algorithim
    computer = random.randint(0,2)
    if computer==0:
        computer = "s"
    elif computer== 1:
        computer = "f"
    elif computer == 2:
        computer = "c"
    
    #risultato finale
    if player_choice == computer:
        print("Pareggio")
        print("Grazie per aver giocato!")
        break
    elif player_choice =="s" and computer=="f" or player_choice=="f" and computer=="c" or player_choice=="c" and computer=="s":
        print("hai vinto!")
        print("Grazie per aver giocato!")
        break
    else:
        print("Ha vinto il computer, sarà per la prossima volta.")
        print("Grazie per aver giocato!")
        break
    
print("exiting program!")

time.sleep(1)
