#!/usr/bin/env python3

# EXERCICE : Question avec la fonction input.

hello = input("Hey ! How are you today ? ")
print(hello)

# EXERCICE : Demander la date de naissance de l'utilisateur et lui dire son âge dans 2 ans.

birthDate = input("En quelle année êtes-vous né ? ")
birthDate = int(birthDate)
currentYear = 2021 - birthDate
dateAfterTwoYears = currentYear + 2
print ("Dans deux ans vous aurez " + str(dateAfterTwoYears) + " ans.")