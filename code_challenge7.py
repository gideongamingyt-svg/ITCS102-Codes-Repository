c = 5 

for a in range(1, c + 1):
    print(" " * (c - a) + "* " * a)

for a in range(c - 1, 0, -1):
    print(" " * (c - a) + "* " * a)