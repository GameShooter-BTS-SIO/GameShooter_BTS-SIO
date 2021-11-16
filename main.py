import keyboard
import os
import random
import time

#\033[",cpt3, ";1H"
class player:
    vie = 20
    attaque = 5
    apparence = "/-\ \n"
    tir = " |"
    espace="\n\n\n"
    espace2=""


class ennemis:
    vie = 10
    attaque = 2
    apparence = "\_/\n"


pseudo = str(input("Entrer votre pseudo.\n"))
for cpt1 in range(5):
    cpt2 = 5 - cpt1
    clear = lambda: os.system('cls')
    clear()
    print("Bienvenu", pseudo, "\nVous avez", player.vie, "points de vie.\n")
    print("La partie commence dans", cpt2, "secondes.")
    time.sleep(1)
clear = lambda: os.system('cls')
clear()


espace=str()
clear = lambda: os.system('cls')
clear()
jeu = True
cpt = 1

while jeu == True:

    clear = lambda: os.system('cls')
    clear()

    print(ennemis.apparence)
    

    if keyboard.is_pressed("t"):
        player.espace="\n\n\n\n\n"
        player.espace2=""
        clear = lambda: os.system('cls')
        clear()
        
        for cpt3 in range(0, 5):
            print(player.espace , player.tir)
            print(player.espace2 , player.apparence)
            player.espace=player.espace[2:]
            if cpt3<=2 :
                player.espace2=player.espace2+"\n"
            time.sleep(0.1)
            clear = lambda: os.system('cls')
            clear()

    print("\n\n\n" ,player.apparence)

    if keyboard.is_pressed("q"):
        clear = lambda: os.system('cls')
        clear()

        if cpt < 50:
            cpt = cpt + 1
            player.apparence = " " + player.apparence
            player.tir = " " + player.tir
            print(player.apparence)

    if keyboard.is_pressed("p"):
        clear = lambda: os.system('cls')
        clear()

        if cpt >= 2:
            cpt = cpt - 1
            player.tir = player.tir[1:]
            player.apparence = player.apparence[1:]
            print(player.apparence)
