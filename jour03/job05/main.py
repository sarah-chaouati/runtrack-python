import re
import matplotlib.pyplot as plot


f = open("jour03/job02/data.txt", "r")
fichier = re.findall("[\w']", f.read().lower())


letters = {}
countL = 0

#pour chaque mot dans le fichier
for word in fichier:
    #pour chaque lettre dans le mot
    for lettre in word:
        #lister les lettres trouver
        if lettre in letters.keys():
            #add la lettre 
            letters[lettre] += 1
        else:
            #continuer
            letters[lettre] = 1

        countL = countL + 1
 

for l in letters:
    #calcul pour donner le %
    letters[l] = (letters[l] * 100) / countL


x = letters.keys()
y = letters.values()

plot.bar(x,y)
plot.savefig("jour03/job05/try.png")
