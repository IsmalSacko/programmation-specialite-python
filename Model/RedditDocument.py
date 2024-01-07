from Model.Document import Document

# classe fille permettant de modéliser un Document Reddit

class RedditDocument(Document):
    # constructeur
    def __init__(self, titre, auteur, date, url, texte):
        Document.__init__(self, titre, auteur, date, url, texte)
        self.setType("Reddit")
        
    def __str__(self):
        return self.getType,": ",self.getTitre()
    
    