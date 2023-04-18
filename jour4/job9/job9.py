L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialiser le maximum et le minimum
maximum = L[0]
minimum = L[0]

# Parcourir la liste et mettre à jour le maximum et le minimum
for nombre in L:
    if nombre > maximum:
        maximum = nombre
    elif nombre < minimum:
        minimum = nombre

# Afficher le maximum et le minimum
print("Maximum dans la liste :", maximum)
print("Minimum dans la liste :", minimum)