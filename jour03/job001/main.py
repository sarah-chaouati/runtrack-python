import re

        #ouverture et lecture du fichier xml
fichier = open("jour03/job001/domains.xml", "r")
l = fichier.read()
# print(l)

print(str(len(re.findall('([.][a-z]{2,4})\W', l))))
       
       
       
       


 