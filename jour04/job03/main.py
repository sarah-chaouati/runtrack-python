nb = int(input("Nombre : "))
pw = int(input("Puissance : "))

def power(nb, pw):
    if pw == 1:
        x = nb
    if (pw > 1):
        x = nb * power(nb, pw - 1)
    return x

print(power(nb, pw))
