from pymongo import*

class Partie_database:
    def __init__(self):
        self.url = "mongodb+srv://botdiscord:botdiscord2025@databasejeu.sklp0ra.mongodb.net/?appName=databasejeu"
        self.client=MongoClient(self.url)
        self.db=self.client["Jeu_de_dames"]
        self.Games=self.db["Games"]
        self.nb= self.Games.count_documents({})
        self.name=f"Partie {self.nb+1}"
        self.coup=[]
        self.nb_coup=0
        self.winner=None
    def winner(self,winner:str):
        self.winner=winner
    def coups(self,coup_joue:str):
        self.coup.append(coup_joue)
        self.nb_coup+=1
    def dict(self):
        self.dic={"Name":self.name,"Winner":self.winner,"Nb coup":self.nb_coup}
        for j in range(len(self.coup)):
                self.dic[f"Coup {j+1}"]=f"{self.coup[j]}  /  {j+1}"
    def add_data(self):
        print(self.dic)
        self.Games.insert_one(self.dic)

Partie=Partie_database()
Partie.coups("G:B8")

#dict=Partie.dic()
#Partie.Games.insert_one(dict) #test 
#Partie.Games.delete_one({"Name":"Partie 1"})
#print(dict)
