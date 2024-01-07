# Classe Document pour stocker les informations d'un document
class Document:
    
    def __init__(self, titre, auteur, date, url, texte):
        """
        Initialise un objet Document avec les informations spécifiées.

        Args:
        titre (str): Le titre du document.
        auteur (str): L'auteur du document.
        date (str): La date du document.
        url (str): L'URL du document.
        texte (str): Le contenu textuel du document.
        """
        self._titre = titre
        self._auteur = auteur
        self._date = date
        self._url = url
        self._texte = texte
        self._type = ""
        
    # Getters
    def getTitre(self):
        # Renvoie le titre du document.
        return self._titre
    
    def getAuteur(self):
        #Renvoie l'auteur du document.
        return self._auteur
    
    def getDate(self):
        """Renvoie la date du document."""
        return self._date
    
    def getUrl(self):
        """Renvoie l'URL du document."""
        return self._url
    
    def getText(self):
        """Renvoie le contenu textuel du document."""
        return self._texte
    
    def getType(self):
        """Renvoie le type du document."""
        return self._type
    
    # Setters
    def setTitre(self, titre):
        """Définit un nouveau titre pour le document."""
        self._titre = titre
    
    def setAuteur(self, auteur):
        """Définit un nouvel auteur pour le document."""
        self._auteur = auteur
    
    def setDate(self, date):
        """Définit une nouvelle date pour le document."""
        self._date = date
    
    def setUrl(self, url):
        """Définit une nouvelle URL pour le document."""
        self._url = url
    
    def setText(self, texte):
        """Définit un nouveau contenu textuel pour le document."""
        self._texte = texte
    
    def setType(self, typ):
        """Définit un nouveau type pour le document."""
        self._type = typ
        
    def __str__(self):
        """Renvoie le titre du document lorsqu'il est converti en chaîne de caractères."""
        return self.getTitre()
