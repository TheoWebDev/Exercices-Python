#!/usr/bin/env python 3

# LES LISTES :

# NE PAS OUBLIER DE FAIRE  : print(fav_alcool[1]) pour afficher l'élément !

fav_alcool = ["Rhum", "Rhum arrangé", "Cidre", "Bière", "Limoncello"]
fav_apero = ["Olives", "Mini Pizza", "TUC", "Saucisson", "Chorizo"]

# Récupérer l'index 1 de la LISTE fav_alcool, renvoie "Rhum arrangé"
fav_alcool[1]

# Récupérer les deux derniers éléments de la LISTE fav_apero, renvoie "Saucisson" et "Chorizo" :
fav_apero[-2:]

# Récupérer les trois premiers éléments de la LISTE fav_apero, renvoie "Olives", "Mini Pizza" et "TUC" :
fav_apero[:3]

# Connaître le nombre d'éléments dans la LISTE, renvoie "5" :
len(fav_alcool)

# Tester qu'un élément est dans la LISTE avec la fonction in et not in :
"Rhum" in fav_alcool
"Vodka" in fav_alcool
"TUC" not in fav_apero
"3D" not in fav_apero
# IN : le 1er renvoie TRUE car Rhum dans la LISTE, le 2ème renvoie FALSE car Vodka pas dans la LISTE
# NOT IN : 1e 1er renvoie FALSE car TUC dans la LISTE, le 2ème renvoie TRUE car 3D pas dand la LISTE

# Sortir les données d'une liste et les afficher :
print("Voici la liste de mes alcools préférés:")
for i, alcool in enumerate(fav_alcool):
    print(str(i+1) + " : " + alcool)

# Modifier un élément de la LISTE :
fav_alcool[2] = "Cidre brut"
# print(fav_alcool)

# Ajouter un élément dans la LISTE avec la fonction append :
fav_alcool.append("Eau")
# print(fav_alcool)

# -----------

# LES DICTIONNAIRES :

# CREER du dictionnaire phone :
phone = { "Alice":   "06 93 28 14 03",
          "Bob":     "06 84 19 37 47",
          "Charlie": "04 92 84 92 03"  }

# AFFICHER la valeur du dictionnaire phone, renvoie le tel d'Alice :
phone["Alice"]

# MODIFIER le numéro en cas d'erreur, va écraser l'ancienne valeur :
phone["Alice"] = "06 01 02 03 04"
# print(phone["Alice"])

# AJOUTER une clé + valeur au dictionnaire phone :
phone["Michel"] = "02 35 10 20 35"
# print(phone)

# POUR TESTER SI UNE VALEUR EST DANS LE DICTIONNAIRE, ON REPREND "in" et "not in" COMME POUR LES LISTES

# AFFICHER toutes les clés (prénoms) du dictionnaire :
for name in phone:
    print("Je connais le numéro de " + name)

# AFFICHER toutes les valeurs (numéros) du dictionnaire :
for phone_number in phone.values():
    print("Quelqu'un a comme numéro " + phone_number)

# AFFICHER les clés et les valeurs du dictionnaire :
for name, phone_number in phone.items():
    print("Le numéro de " + name + " est " + phone_number)

# CONSTRUCTION d'un sous-dictionnaire dans un dictionnaire (comme les tableaux à 2 dimensions)
contacts = { "Alice":  { "phone": "06 93 28 14 03",
                         "email": "alice@megacorp.eu" },

             "Bob":    { "phone": "06 84 19 37 47",
                         "email": "bob.peterson@havard.edu.uk" },

             "Charlie": { "phone": "04 92 84 92 03" } }

# RECUPÉRER le numéro de Bob
contacts["Bob"]["phone"]

# AJOUTER le mail de Charlie
contacts["Charlie"]["email"] = "charlie@orange.fr"

# AJOUTER Deborah avec juste une adresse mail
contacts["Deborah"] = {"email": "deb@hotmail.fr"}