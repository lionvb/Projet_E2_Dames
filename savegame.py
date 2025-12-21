from pymongo import*

class Partie_database:
    """Classe pour gérer la base de bonnée héberger en ligne"""
    def __init__(self,player1,player2):
        """Initialisation de la database, se connecter et définir les variables"""
        self.url = "mongodb+srv://botdiscord:botdiscord2025@databasejeu.sklp0ra.mongodb.net/?appName=databasejeu" #url de la base de donnée
        self.client=MongoClient(self.url) #Connexion à la base de donnée
        #Création ou accès au collections et documents de la base de données
        self.db=self.client["Jeu_de_dames"] 
        self.Games=self.db["Games"]
        self.nb= self.Games.count_documents({}) #Pour savoir le nombre de partie déja stocké
        self.name=f"Partie {self.nb+1}" #Pour le numérotage des parties
        self.coup=[] #Intialisation d'une liste vide pour stocker les coups
        #Variable pour stocker les infos
        self.nb_coup=0
        self.player1=player1
        self.player2=player2
        self.winner=None 
    def winner(self,winner:str):
        """Définir le winner qd une partie est fini"""
        self.winner=winner
    def coups(self,coup_joue:str):
        """Ajout des coups à la liste our les stocker avec le nombre de coups """
        self.coup.append(coup_joue)
        self.nb_coup+=1
    def dict(self):
        """Mise en place du dictionnaire pour stocker sur la database"""
        self.dic={"Name":self.name,"Winner":self.winner,"Player1":self.player1,"Player2":self.player2,"Nb coup":self.nb_coup}
        for j in range(len(self.coup)):
                self.dic[f"Coup {j+1}"]=f"{self.coup[j]}  /  {j+1}" #j+1 est une sorte de timestamp
    def add_data(self):
        """Envoyer les données sur la database"""
        print(self.dic)
        self.Games.insert_one(self.dic)