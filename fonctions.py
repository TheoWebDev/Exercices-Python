#!/usr/bin/env python3

# EXERCICE : Fonction qui renvoie l'âge en fonction de l'année de naissance à partir de 2021

def annee_naissance(age):
    return 2021 - age

print(annee_naissance(1992))

# EXERCICE : Fonction pour centrer un mot sur 40 caractères

def center(word):
    # calcul du nombre de caractère avec la fonction len
    space = len(word)
    # calcul du nombre d'espace restant sur 40 moins le mot saisi
    middle = 40 - space
    # on divise le restant par 2 pour les 2 espaces sur le côté
    result = int(middle / 2)
    # on retourne le résultat en multipliant les espaces
    return " " * result + word + " " * result

print("|" + center("Python") + "|")

# EXERCICE : Fonction pour encadrer un mot

def encrader(mot, largeur = 40, caractere = "#"):
    return largeur * caractere + "\n" + encrader (mot, largeur) + "\n"

# EXERCICE : Fonction date de naissance avec des conditions

def annee_naissance(age):
    if age <= 0 or age >= 130:
        print("NOPE")
    elif age:
        print("OKAY")
    elif age:
        check = isinstance("toto", str)
        print(check)
    return age

print(annee_naissance("toto"))