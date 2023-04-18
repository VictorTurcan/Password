def distance_toilettes(marches, hauteur):
    hauteur_m = hauteur / 100.0  # conversion de la hauteur des marches en mètres
    distance = marches * hauteur_m * 2 * 5 * 7  # distance totale en mètres
    distance_arrondie = round(distance, 2)  # arrondi à deux décimales
    message = f"Pour {marches} marches de {hauteur} cm, le gardien parcourt {distance_arrondie} m par semaine."
    return message
marches = 100
hauteur = 20
message = distance_toilettes(marches, hauteur)
print(message)