# on importe le module random pour faire des choses au hasard
import random

# on importe le module time pour gerer le temps sur le jeu
import time

# afficher de message de bienvenue
print ("Bienvenue au jeu du juste prix, tu dois deviner le prix de l'article choisi \n Le prix est entre 1 et 100")

#choisir un nombre entre 1 et 100
nombre_hasard = random.randint(1,100)
nombre_proposition = 0

#compteur tentatives
tentatives = 10

#boucle tant que
while nombre_proposition != nombre_hasard and tentatives > 0:

    # proposer au joueur d'entrer une valeur
    print("Entrez votre proposition: ")

    proposition = input()

    #verif texte
    if proposition.isdigit():
        
        #transformer proposition en entier
        nombre_proposition = int(proposition)

        if nombre_proposition < nombre_hasard:
            print("C'est plus")
        elif nombre_proposition > nombre_hasard:
            print("C'est moins")

        tentatives -=1
        print("Tentatives:", tentatives)
           
    else:
        print("Tu dois entrer un nombre")

if tentatives == 0:
    print("Perdu ! , tu n'as plus assez d'essais. Le nombre était", nombre_hasard )
else:
    print("Tu as trouvé, Bravo !")