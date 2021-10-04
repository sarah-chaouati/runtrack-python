import re
import matplotlib.pyplot as plot


f = open("jour03/job02/data.txt", "r")
fichier = re.findall("[\w']+", f.read().lower())

wordsL = {}
countW = 0

for word in fichier:
    if len(word) in wordsL.keys():
        wordsL[len(word)] += 1
    else:
        wordsL[len(word)] = 1

    countW = countW + 1

for l in wordsL:
    #print(l)
    #print(wordsLenght)
    wordsL[l] = (wordsL[l] * 100) / countW

x = wordsL.keys()
y = wordsL.values()

plot.bar(x,y)
plot.savefig("jour03/job08/try.png")

