
n1 = int(input(" n*1 : "))
n2 = int(input(" n*2 : "))
n3 = int(input(" n*3 : "))
n4 = int(input(" n*4 : "))
n5 = int(input(" n*5 : "))

def Ask (n1, n2, n3, n4, n5):
        data = [n1, n2, n3, n4, n5]
        data.sort()
        
        return "Votre saisie  : {} ".format(data)

print(Ask(n1, n2, n3, n4, n5))



