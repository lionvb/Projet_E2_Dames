from pymongo import*
client=MongoClient('mongodb://localhost:27017')
db=client["Jeu_de_dames"]
Games=db["Games"]
i=count = Games.count_documents({})
class Partie:
    def __init__(self,i:int):
        self.nb=i
        self.name=f"Partie {i+1}"
        self.coup=[]
        self.nb_coup=0
        self.winner=None
    def winner(self,winner:str):
        self.winner=winner
    def coups(self,coup_joue:str):
        self.coup.append(coup_joue)
        self.nb_coup+=1
    def dic(self):
        self.dic={"Name":self.name,"Winner":self.winner,"Nb coup":self.nb_coup}
        for i in range(len(self.coup)):
                self.dic[f"Coup {i+1}"]=self.coup[i]
        return self.dic
Parti=Partie(i)
Parti.coups("G:B8")
print(Parti.dic())
#Games.delete_one({"Name":"Partie"})
#Games.insert_one(Parti.__dic__()) #test 