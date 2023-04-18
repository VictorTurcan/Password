def chiffrement_cesar(message, decalage):
    message_chiffre = ''
    for lettre in message:
        # Vérifie si la lettre est une lettre de l'alphabet
        if lettre.isalpha():
            # Calcule l'indice de la lettre décalée dans l'alphabet
            indice_lettre_decalee = (ord(lettre.lower()) - 97 + decalage) % 26
            # Calcule la lettre décalée en fonction de l'indice
            lettre_decalee = chr(indice_lettre_decalee + 97)
            # Ajoute la lettre décalée au message chiffré
            message_chiffre += lettre_decalee if lettre.islower() else lettre_decalee.upper()
        else:
            # Ajoute la lettre telle quelle si ce n'est pas une lettre de l'alphabet
            message_chiffre += lettre
    return message_chiffre
message = "Le message secret du job 4 "
decalage = 3
message_chiffre = chiffrement_cesar(message, decalage)
print(message_chiffre)