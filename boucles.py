#!/usr/bin/env python3

# EXERCICE : Boucle FOR table de multiplication

def table_multiplication(number, maxCalcul = 11):
    for i in range(1, maxCalcul):
        print(i, " x ", number, " = ", i * number)

# Fonction range pour le calcul d'un nombre entier
# Ne pas utiliser print pour appeler la fonction table_multiplication

table_multiplication(8)