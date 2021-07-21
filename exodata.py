#!/usr/bin/env python 3

# EXEMPLE pour afficher les animaux qui mesurent plus d'un mètre.

mes_animaux = { "girafe": 300,    "coyote": 50,
                 "chenille": 3,       "cobra": 45}

def au_moins_un_metre(animaux):

    for animal, taille in animaux.items():
        if taille >= 100:
            yield animal


for animal in au_moins_un_metre(mes_animaux):
    print("La " + animal + " mesure plus d'un mètre !")

# # Sortir le plus grand nombre d'une liste :

x = [5, 9, 12, 6, -1, 4]

def plus_grand(ma_liste):
    nombre_le_plus_grand = ma_liste[0]
    for nombre in ma_liste:
        if nombre > nombre_le_plus_grand:
            nombre_le_plus_grand = nombre
    return nombre_le_plus_grand

print(plus_grand(x))

# Fonction qui calcule la somme d'une liste de nombre :

a = [3, 5, 9]
def somme(liste):
    somme = 0
    for nombre in liste:
        somme = nombre + somme
    return somme

print(somme(a))


mon_path = "/usr/bin/toto.py"
mon_path = mon_path.split("/")[1:]