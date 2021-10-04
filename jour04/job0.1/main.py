val = int(input("Valeur : "))

def recursive(val):
    if val == 0:
        return 1
    else:
        print( val * recursive(val - 1))

if val < 0:
    print("Error")
else:
    print("Resultat :",recursive(val))
    
