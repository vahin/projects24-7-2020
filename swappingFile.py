def swap(x, y):
    f = open(x, "r")
    fCont = f.readlines()
    f2 = open(x, "w")
    g = open(y, "r")
    gCont = g.readlines()
    g2 = open(y, "w")
    f2.writelines(gCont)
    g2.writelines(fCont)

# swap("sample1.txt", "sample2.txt")
swap(input("Enter the path of your file: "), input("Enter the path of your file you want to swap with: "))
