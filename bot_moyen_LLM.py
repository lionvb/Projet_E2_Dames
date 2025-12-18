import json
from groq import Groq
from game import *


# --- Constantes du Jeu ---
White = 1
White_lady = 2
Black = 3
Black_lady = 4

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
    client = None

SYSTEM_PROMPT_FR = (
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
    # Exemple d'un coup valide sur la ligne 6 vers la ligne 5 (qui doit être vide)
    "Exemple de coup d'ouverture valide pour les BLANCS : {'r1': 6, 'c1': 0, 'r2': 5, 'c2': 1}. "
    "N'ajoutez AUCUN texte ou explication, SEULEMENT l'objet JSON."
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
    if my_game.current_player == "White" :
        result_white = my_game.llm_move(client, SYSTEM_PROMPT_FR)
        print(f"\nCouleur jouée: Blanc\nRésultat: {result_white}")

    print("\n--- Plateau Après le Coup de l'IA (Blanc) ---")
    print(my_game.board)
    print("-" * 25)

    """
 # L'IA (Groq) joue le tour des Noirs
    if my_game.current_player == "Black" :
        # --- BLOC JOUEUR HUMAIN (NOIR) ---
        print("\n--- C'EST À VOUS DE JOUER (NOIR) ---")

        # Vous pouvez demander les coordonnées en ligne de commande :
        move_input = input("Entrez votre coup (r1,c1,r2,c2): ")

        try:
            r1, c1, r2, c2 = map(int, move_input.split(','))
            result_black = my_game.moves(r1, c1, r2, c2)
            print(f"Résultat du coup Noir: {result_black}")

        except:
            print("Entrée invalide. Le jeu doit être redémarré.")
            result_black = "Échec du coup humain"
        """

    print("\n--- Plateau Après le Coup de l'IA (Noir) ---")
    print(my_game.board)
    print(f"Prochain joueur : {'Blanc' if my_game.current_player == "White" else "Noir"}")