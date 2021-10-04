import re
# ouverture et lecture du fichier xml
fichier = open("jour03/job02/data.txt", "r")
l = fichier.read()
# print(l)

word_list = re.findall("[\W]+", l)
print(len(word_list))


