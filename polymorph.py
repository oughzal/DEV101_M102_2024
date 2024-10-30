class EmptyClass:
    pass # classe définie mais vide

class Stagiaire:
    groupe = "DE101" # attribut de classe

    def __init__(self, nom, prenom): # constructeur
        self.nom = nom # attribut d'instance
        self.prenom = prenom # attribut d'instance
    
    def __del__(self): # destructeur
        print(f"objet détruit: {self.nom} {self.prenom}")

    def affiche(self): # méthode d'instance
        print(f"{self.nom} {self.prenom} est dans le groupe {self.groupe}")
    @classmethod
    def change_groupe(cls, groupe): # méthode de classe
        cls.groupe = groupe
    
Stagiaire1 = Stagiaire("Doe", "John") # instanciation
Stagiaire2 = Stagiaire("Doe", "Jane") # instanciation
Stagiaire3 = Stagiaire1 # nouvelle référence à Stagiaire1

