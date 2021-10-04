class Personne:
    
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    

class Auteur(Personne):
    
    def __init__(self, nom, prenom):
        Personne.__init__(self,nom,prenom)
        self.oeuvre = []
        
    def ecrireUnLivre(self, titre):
        self.oeuvre.append(titre)

    def listerOeuvre(self):
        print (self.oeuvre)
    
    def getInfoAuteur(self):
        print(self.nom, self.prenom, self.oeuvre)


class Livre():
    
    def __init__(self, titre, auteur: Auteur):
        self.titre = titre
        self.auteur = auteur

    def showBook(self):
        print(self.titre)
 

class Client(Personne):
    
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.collection = []
        
    def inventaire_client(self):
        print("Inventaire Client",self.collection)

    def getInfoClient(self):
        print("Info Client",self.nom, self.prenom, self.collection)


class Bibliotheque (Auteur,Client):
    
    def __init__(self, nomCat):
        self.nomCat = nomCat
        self.catalogue = []
        
    def acheterLivre(self, auteur : Auteur, titreAchat, qtLivre: int):
        
        if titreAchat in auteur.oeuvre:
            print("Achat en cours")
            self.catalogue.append({'titre': titreAchat,'qt': qtLivre})
        else:
            print("Not found :( ")
       
    def inventaire(self):
        print("Inventaire Shop",self.catalogue)
        
    def louer(self, client : Client, titre):
        # print(self.catalogue)
        for i in self.catalogue:
            if titre == i['titre']:
                client.collection.append({'titre': titre})
                i['qt'] = i['qt'] - 1
                print("Location ok")
           
                   
    def rendreUnLivre(self, client: Client, titre):
        
        for i in client.collection:
            if titre == i['titre']:     
                print("Livre rendu")
                client.collection.remove({'titre': titre})
            else:
                print("nop")
            
            for k in self.catalogue:
                if titre == k['titre']:
                    k['qt'] = k['qt'] + 1

                       

                    
       

        
    

# Crea Bibliotheque
shop = Bibliotheque("Random")
#Auteur
pinou = Auteur("Pinou","LeLapin")
# Crea Livre
pinou.ecrireUnLivre("Passion Fraise")
pinou.ecrireUnLivre("Pinouterie")
#Lister info auteur
pinou.listerOeuvre()
pinou.getInfoAuteur()
# #Remplissage du stock du shop
shop.acheterLivre(pinou,'Pinouterie',int(5))
shop.acheterLivre(pinou,'Passion Fraise',int(5))
#Inventaire shop
shop.inventaire()
#Client
mimi = Client("Mimi", "LeChat")
#Location
shop.louer(mimi,'Pinouterie')
# Visualisation inventaire client& shop
mimi.inventaire_client()
shop.inventaire()
#Rendre livre
shop.rendreUnLivre(mimi,'Pinouterie')
# Visualisation inventaire client& shop
mimi.inventaire_client()
shop.inventaire()

