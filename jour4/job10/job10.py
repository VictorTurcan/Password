L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialiser le produit à 1
produit = 1

# Parcourir la liste et multiplier les nombres compris entre 25 et 90 inclusivement
for nombre in L:
    if 25 <= nombre <= 90:
        produit *= nombre

# Afficher le produit
print("Le produit des nombres compris entre 25 et 90 dans la liste est :", produit)