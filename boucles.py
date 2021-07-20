#!/usr/bin/env python3

# EXERCICE : Boucle FOR table de multiplication

# def table_multiplication(number, maxCalcul = 11):
#     for i in range(1, maxCalcul):
#         print(i, " x ", number, " = ", i * number)

# Fonction range pour le calcul d'un nombre entier
# Ne pas utiliser print pour appeler la fonction table_multiplication

# table_multiplication(9)

# EXERCICE : Demander un mot de passe pour rentrer dans la boucle

def table_with_password():
    password = input("Enter your password ? ")
    while password != "python":
        password = input("Enter your password ? ")
    i = 1
    while i < 6:
        print(i)
        i += 1

table_with_password()

# Tant que le bon mdp n'est pas donné, 1ère boucle while, si bon mdp, affiche 2ème boucle while