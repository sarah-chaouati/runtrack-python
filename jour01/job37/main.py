wrd = input("Add mot ") #recuperer l'entrée 
# wrd = list(input("add mot")) #recuperer l'entrée en list

# def Mix(wrd):

# a = sorted(wrd) #tri des lettres



for i in wrd : #boucle autant de fois que de lettre ! 
    if i.isupper():
        print("Erreur: Majuscule ")
        exit()
    elif i.isalnum():
        print("Erreur: Special Char et espace non accepter")
        exit()
    else:
        print("suite du code")

# Mix(wrd)



