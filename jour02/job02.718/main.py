class Personne:
    
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        


class Auteur(Personne):
    
    def __init__(self, nom, prenom):
        self.oeuvre = []
        
    
    def listerOeuvre(self):
        return (print(self.oeuvre))
        
    
    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre.titre)
        


class Livre(Auteur):
    
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        

#Auteur
pinou = Auteur("Pinou","LeLapin")
#Livre
pinou.ecrireUnLivre("Passion Fraise")
pinou.ecrireUnLivre("Pinouterie")
#Lister
pinou.listerOeuvre()





