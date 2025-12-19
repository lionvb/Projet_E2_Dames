import os
import json
from groq import Groq
from game import *

class DraughtsBot:
    def __init__(self):
        
        key = os.environ.get("GROQ_API_KEY")
        
        if not key:
            print("erreur : La variable d'environnement GROQ_API_KEY est manquante !")
            self.client = None
        else:
            try:
                self.client = Groq(api_key=key)
                print("client Groq initialisé avec succès ")
            except Exception as e:
                print(f"erreur d'initialisation Groq : {e}")
                self.client = None
                

        self.system_prompt = (
            "Vous êtes un joueur de dames internationales (10x10) de classe mondiale. "
            "Votre tâche est d'analyser l'état actuel du plateau et de suggérer le meilleur coup à jouer. "
            "Le plateau est une grille 10x10, les coordonnées sont (ligne, colonne) de 0 à 9. "
            "Le joueur actuel est UNIQUEMENT BLANC (W). Les pièces BLANCHES se trouvent aux LIGNES 6, 7, 8 et 9. "
            "Elles doivent se déplacer vers le HAUT (lignes inférieures vers lignes supérieures) et en DIAGONALE. "
            "ATTENTION : Les DAMES se jouent uniquement en DIAGONALE ! Pour un coup de pion 1x1, cela signifie que le déplacement (r1, c1) -> (r2, c2) DOIT AVOIR |r1-r2| = 1 et |c1-c2| = 1. "
            "ÉTANT DONNÉ QUE C'EST LE PREMIER COUP DE L'OUVERTURE ET QU'IL N'Y A PAS DE CAPTURES POSSIBLES, "
            "VOUS DEVEZ JOUER UN DÉPLACEMENT SIMPLE DIAGONAL DE 1x1, en bougeant un pion de la LIGNE 6 vers la LIGNE 5. "
            "Vous DEVEZ répondre UNIQUEMENT avec un objet JSON qui suit EXACTEMENT cette structure : "
            "{'r1': ligne_départ, 'c1': col_départ, 'r2': ligne_arrivée, 'c2': col_arrivée}. "
            "Exemple d'un coup d'ouverture valide pour les BLANCS : {'r1': 6, 'c1': 0, 'r2': 5, 'c2': 1}. "
            "N'ajoutez AUCUN texte ou explication, SEULEMENT l'objet JSON."
        )


    def jouer_coup_ia(self, instance_jeu):
        """
        instance_jeu doit être un objet de la classe Game().
        Cette fonction appelle llm_move que tu as déjà définie dans Game.
        """
        if self.client is None:
            return "Erreur : Client Groq non disponible."
        
      
        resultat = instance_jeu.llm_move(self.client, self.system_prompt)
        return resultat