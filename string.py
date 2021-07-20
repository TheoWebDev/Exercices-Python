#!/usr/bin/env python3

# EXERCICE : Demander un mot à l'utilisateur et lui dire combien il comporte de caractère.

word = input("Entrez un mot pour connaitre le nombre de caractère ; ")
number = len(word)
numberHash = "#" * (number + 4)

print("Le mot " + word + " contient " + str(number) + " caractères.")
print(numberHash + "\n# " + word + " #\n" + numberHash)

# Calcul du nombre de caractère avec la fonction len
# Conversion de la variable number qui est en int, en string
# Variable numberHash et deuxième print pour encadrer le mot