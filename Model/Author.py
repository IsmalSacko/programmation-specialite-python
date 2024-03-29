# classe Author qui représente : name, ndoc, production

class Author:

    def __init__(self, name, ndoc=0, production={}):
        self._name = name
        self._ndoc = ndoc
        self._production = production

    # getter
    def getName(self):
        return self._name

    def getNdoc(self):
        return self._ndoc

    def getProduction(self):
        return self._production

    # setter
    def setName(self, name):
        self._name = name

    def addProd(self, prod):
        self._production[self._ndoc] = prod
        self._ndoc += 1

    # Méthode qui renvoie True si le document donné est écrit par l'auteur.    
    def writtenDoc(self, doc):
        return doc in self._production.values()

    # Affichage
    def __str__(self):
        return self.getName()
