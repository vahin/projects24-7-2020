# Check other programs of this folder
def hcf(x, y):
    if (x > y):
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf

print("HCF of 10 and 5:", hcf(10, 5))
