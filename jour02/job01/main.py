class Personne:
    def __init__(self, prenom='random', nom='people'):
        self.prenom = prenom
        self.nom = nom
    
    def get_prenom(self):
        return self.prenom
    
    def get_nom(self):
        return self.nom
    
    def set_prenom(self, prenom):
        self.prenom = prenom
    
    def set_nom(self, nom):
        self.nom = nom
        
    def SePresenter(self):
        print(self.prenom, self.nom)


# p1
Mimi = Personne('Mimi', 'LeChat')
Mimi.SePresenter()

# use mutateur
personne = Personne()
personne.set_prenom('Mimi')
personne.set_nom('Le retour')
personne.SePresenter()