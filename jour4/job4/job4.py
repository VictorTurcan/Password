def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange, Melon"]
    fruits.insert(2, "Mangue")
    return fruits
ma_liste_de_fruits = ajouter_mangue()
print(ma_liste_de_fruits)