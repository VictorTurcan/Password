def modification_mot(mot):
    # Vérifier que le mot ne contient que des lettres minuscules de l'alphabet
    if not mot.isalpha() or not mot.islower():
        print("Le mot doit contenir uniquement des lettres minuscules de l'alphabet.")
        return
    
    # Transformer le mot en liste de caractères
    liste_mot = list(mot)
    
    # Trouver la première paire de caractères qui n'est pas dans l'ordre alphabétique
    i = len(liste_mot) - 1
    while i > 0 and liste_mot[i - 1] >= liste_mot[i]:
        i -= 1
    
    if i == 0:
        # Le mot est déjà le dernier dans l'ordre alphabétique
        print("Le mot est déjà le dernier dans l'ordre alphabétique.")
        return
    
    # Trouver le plus petit caractère dans le suffixe du mot qui est plus grand que le caractère i-1
    j = len(liste_mot) - 1
    while liste_mot[j] <= liste_mot[i - 1]:
        j -= 1
    
    # Échanger les caractères i-1 et j
    liste_mot[i - 1], liste_mot[j] = liste_mot[j], liste_mot[i - 1]
    
    # Inverser le suffixe du mot après le caractère i-1
    liste_mot[i:] = reversed(liste_mot[i:])
    
    # Transformer la liste de caractères en mot et le retourner
    nouveau_mot = ''.join(liste_mot)
    return nouveau_mot