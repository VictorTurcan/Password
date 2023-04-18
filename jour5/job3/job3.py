def draw_carpet(n):
    for i in range(n, -1, -1):
        for j in range(n, -1, -1):
            if i == j:
                print("", end="")
            elif j+i == n:
                print(end='' ' ')
            else:
                print("", end="#")
        print()
draw_carpet(10)