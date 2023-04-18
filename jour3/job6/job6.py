s = "abcdefghijklmnopqrstuvwxyz" * 10
n_lines = 10

for i in range(1, n_lines +):

    chars_to_print = s[:i*2 - 1]
    padding = n_lines - i
    print(" " * padding + chars_to_print + " " * padding)

chaine = "nikana"
chaine_inverse = chaine[::-1]
print(chaine_inverse)