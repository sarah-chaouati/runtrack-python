import re
val = int(input("Valeur(int) : "))

# valVerif = val.is_integer()
# print(valVerif) 

# ouverture et lecture du fichier xml
fichier = open("jour03/job02/data.txt", "r")
l = fichier.read()
# print(l)

#regex pour separation des mots
word = re.findall("[\w']+", l)
# print(word)
# print (len(word))


a = 0
i = 0

while i < len(word):
# verif le nombre de lettre de chaque mot  si  = à l'entrée
   if len(word[i]) == val :
# incrementation
       a += 1
   i += 1

print("Resultat", a)
    