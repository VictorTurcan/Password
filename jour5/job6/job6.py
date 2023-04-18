def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        elif note >= 40 and note % 5 >= 3:
            note_arrondie = note + 5 - (note % 5)
            if note_arrondie > 100:
                note_arrondie = 100
            notes_arrondies.append(note_arrondie)
        else:
            notes_arrondies.append(note)
    return notes_arrondies
notes = [32, 67, 81, 46, 72, 90]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)