L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Initialiser la somme à zéro
somme = 0

# Parcourir la liste et ajouter les valeurs paires à la somme
for nombre in L:
    if nombre % 2 == 0:
        somme += nombre

# Afficher la somme des valeurs paires
print("Somme des valeurs paires dans la liste :", somme)