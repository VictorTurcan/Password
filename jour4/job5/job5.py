L = [3, 8, 12, 6, 5]

# Afficher la valeur de L[1]
print(L[1])

# Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
def remplacer_L3():
    L[3] = L[2] + L[4]

remplacer_L3()

# Afficher la valeur du dernier terme de la liste
print(L[-1])