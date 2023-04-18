def my_long_word(n, chaine):
    # Divise la chaîne en une liste de mots
    mots = chaine.split()
    # Initialise la nouvelle chaîne
    nouvelle_chaine = ""
    # Parcourt la liste des mots
    for mot in mots:
        # Si le mot est plus long que n, l'ajouter à la nouvelle chaîne
        if len(mot) > n:
            nouvelle_chaine += mot + " "
    # Retourner la nouvelle chaîne sans l'espace final
    return nouvelle_chaine.strip()

# Exemple d'utilisation
chaine = "Bonjour je suis un étudiant et je suis actuellement en train de travailler sur Visual Studio Code"
n = 3
resultat = my_long_word(n, chaine)
print(resultat)