for a in range(5): 
    for b in range(5):
        if a == 4 or b == 0 or a == 0 or b == 4:
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print()