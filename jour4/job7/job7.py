L = [8, 24, 48, 2, 16]

# Initialiser un compteur à zéro
compteur = 0

# Parcourir la liste et compter les multiples de 3
for nombre in L:
    if nombre % 3 == 0:
        compteur += 1

# Afficher le nombre de multiples de 3 trouvés
print("Nombre de multiples de 3 dans la liste :", compteur)