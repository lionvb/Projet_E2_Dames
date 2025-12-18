from pymongo import*

class Partie_database:
    def __init__(self,player1,player2):
        self.url = "mongodb+srv://botdiscord:botdiscord2025@databasejeu.sklp0ra.mongodb.net/?appName=databasejeu"
        self.client=MongoClient(self.url)
        self.db=self.client["Jeu_de_dames"]
        self.Games=self.db["Games"]
        self.nb= self.Games.count_documents({})
        self.name=f"Partie {self.nb+1}"
        self.coup=[]
        self.nb_coup=0
        self.player1=player1
        self.player2=player2
        self.winner=None
    def winner(self,winner:str):
        self.winner=winner
    def coups(self,coup_joue:str):
        self.coup.append(coup_joue)
        self.nb_coup+=1
    def dict(self):
        self.dic={"Name":self.name,"Winner":self.winner,"Player1":self.player1,"Player2":self.player2,"Nb coup":self.nb_coup}
        for j in range(len(self.coup)):
                self.dic[f"Coup {j+1}"]=f"{self.coup[j]}  /  {j+1}"
    def add_data(self):
        print(self.dic)
        self.Games.insert_one(self.dic)