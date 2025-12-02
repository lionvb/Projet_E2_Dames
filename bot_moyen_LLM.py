import os
import json
from groq import Groq 
from game import * # Importe les classes Piece, Board, Game, etc.

# --- Constantes du Jeu ---
White = 1
White_lady = 2
Black = 3
Black_lady = 4

# La clé codée en dur (utilisée si la variable d'environnement n'est pas trouvée)
DEFAULT_GROQ_API_KEY = "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"

# --- Initialisation du Client Groq ---
try:
    # 1. Tente de charger la clé depuis la variable d'environnement
    key = os.environ.get("GROQ_API_KEY")
    
    # 2. Si la variable d'environnement est vide, utilise la clé par défaut (codée en dur)
    if not key:
        key = DEFAULT_GROQ_API_KEY
    
    # 3. Initialisation unique du client
    client = Groq(api_key=key) 
    print("Client Groq initialisé avec succès.")

except Exception as e:
    print(f"Erreur lors de l'initialisation du client Groq : {e}")
    client = None # Le bot ne fonctionnera pas

# --- Prompts du LLM (Groq) ---
SYSTEM_PROMPT_FR = (
    "Vous êtes un joueur de dames internationales (10x10) de classe mondiale. "
    "Votre tâche est d'analyser l'état actuel du plateau et de suggérer le meilleur coup à jouer. "
    "Le plateau est une grille 10x10, les coordonnées sont (ligne, colonne) de 0 à 9. La ligne 0 est pour les Blancs, la ligne 9 pour les Noirs. "
    "Les symboles sont: W=Pion Blanc, Wk=Dame Blanche, B=Pion Noir, Bk=Dame Noire, .=Case vide. "
    "Le joueur actuel doit jouer. "
    "Vous DEVEZ répondre UNIQUEMENT avec un objet JSON contenant les coordonnées du coup. "
    "Le coup doit être au format : {'r1': ligne_départ, 'c1': col_départ, 'r2': ligne_arrivée, 'c2': col_arrivée}. "
    "N'ajoutez aucune autre explication."
)



# ----------------------------------------------------------------------
# --- TEST ET UTILISATION PRINCIPALE ---
# ----------------------------------------------------------------------

if __name__ == "__main__":
    
    my_game = Game()

    print("--- Plateau Initial ---")
    print(my_game.board)
    print("-" * 25)

    # L'IA (Groq) joue le premier coup (Blancs)
    if my_game.current_player == White:
        # 🟢 CORRECTION : Passer client et SYSTEM_PROMPT_FR en arguments
        result_white = my_game.llm_move(client, SYSTEM_PROMPT_FR) 
        print(f"\nCouleur jouée: Blanc\nRésultat: {result_white}")

    print("\n--- Plateau Après le Coup de l'IA (Blanc) ---")
    print(my_game.board)
    print("-" * 25)
    
    # L'IA (Groq) joue le tour des Noirs
    if my_game.current_player == Black:
        # 🟢 CORRECTION : Passer client et SYSTEM_PROMPT_FR en arguments
        result_black = my_game.llm_move(client, SYSTEM_PROMPT_FR) 
        print(f"\nCouleur jouée: Noir\nRésultat: {result_black}")

    print("\n--- Plateau Après le Coup de l'IA (Noir) ---")
    print(my_game.board)
    print(f"Prochain joueur : {'Blanc' if my_game.current_player == White else 'Noir'}")