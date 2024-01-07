import string 
from nltk.stem.snowball import SnowballStemmer
#from nltk.corpus import stopwords
import re
import numpy as np
from math import log

"""
    Classe Menu utilisée pour représenter un menu de questions et réponses,
    et effectuer des opérations de recherche et d'analyse.

    Attributes:
    - questions (dict): Un dictionnaire contenant les questions du menu.
    - answers (dict): Un dictionnaire contenant les réponses associées aux questions.
    - recherche (str): La chaîne de recherche utilisée pour les calculs.
    - all_words (list): Liste de mots nets extraits des questions pour le traitement.
    - _ndoc (int): Nombre de documents/question dans le menu.
"""
class Menu: 
    

    # Initialise un objet Menu avec les questions, les réponses et une chaîne de recherche spécifiées.
    def __init__(self, questions={}, answers={}, recherche=""):
        self._quest=questions
        self._ans= answers
        self.recherche=recherche
        self.all_words= self._nettoyer(" ".join(list(set(questions.values()))))
        self._ndoc= len(questions)
    # Nettoie le texte donné en retirant la ponctuation, les espaces, en mettant en minuscules,
    # et en appliquant une racinisation (stemming) aux mots.    
    def _nettoyer(self, text):
        ponctuation= string.punctuation
        compiler=re.compile("[%s]" % re.escape(ponctuation))
        text= compiler.sub(" ", text)
        text= text.replace("\n", " ").replace("\t", " ")
        #st= stopwords.words("english")
        texte= text.lower()
        token= texte.split()
        token= list(set([tk for tk in token if tk.isalpha() and len(tk)>1]))
        #token= [tk for tk in token if tk not in st]
        #Pour raciniser les mots
        stemmer=SnowballStemmer("english")
        token=[stemmer.stem(mot) for mot in token]
        return token
    
    # Crée un vocabulaire à partir des questions nettoyées et le renvoie.
    def vocabulary(self):
        voc={k: self._nettoyer(v) for k,v in self._quest.items()}
        return voc
    
    #matrice methode BOW
    # Elle une matrice document-mot pour les mots donnés.
    def matDocMot(self, mots):
        voc= self.vocabulary()
        n=len(voc)
        m= len(mots)
        mat= np.zeros((n, m))
        for i in range(n):
            doc=voc[i]
            for j in range(m):
                mat[i][j]= doc.count(mots[j])
        return mat
    
    #methode tfidf
    # Elle renvoie le score de chaque question dans le menu pour la chaîne de recherche donnée.
    #Calcule le terme fréquence (TF) pour un mot dans un document.
    def _tf(self, doc, mot):
        n= doc.count(mot)
        N= len(doc)
        if N==0:
            return 0
        return n/N
    
    #Calcule l'inverse de la fréquence du document (IDF) pour un mot donné.
    def _idf(self, mot, voc):
        n=0
        for v in voc.values():
            if v.count(mot)>0:
                n+=1
        if n==0:
            return 0
        return log(self._ndoc/n)
    
    #matrice tfidf
    def _matTfIdf(self, mots):
        voc= self.vocabulary()
        n=len(voc)
        m= len(mots)
        mat= np.zeros((n, m))
        for i in range(n):
            doc=voc[i]
            for j in range(m):
                mot=mots[j]
                mat[i][j]= self._tf(doc, mot)*self._idf(mot, voc)
        return mat
    
    #score with tf idf
    def score(self):
        mots= self.all_words
        p= self._nettoyer(self.recherche)
        mat=self._matTfIdf(mots)
        entrer=np.array([p.count(m) for m in mots])
        result= mat@entrer
        if sum(result)==0:
            return 5
        return np.argmax(result)
    
    
    # Méthode de recherche qui renvoie la question la plus pertinente dans le menu pour la chaîne de recherche donnée.
    def response(self, i):
        return self._ans[i]