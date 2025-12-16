import json
from game import Game # Assurez-vous que la classe Game est importée correctement
from ai_player import DraughtsAI # Importation du nouveau module IA

def execute_ai_turn(game_instance: Game, ai_instance: DraughtsAI):
    """Exécute le tour de l'IA."""
    move_data = ai_instance.get_ai_move_data(game_instance)
    
    if move_data is None:
        print("L'IA n'a pas pu suggérer de coup valide.")
        return

    r1 = move_data.get('r1')
    c1 = move_data.get('c1')
    r2 = move_data.get('r2')
    c2 = move_data.get('c2')
    
    print(f"L'IA Groq suggère le coup : ({r1}, {c1}) -> ({r2}, {c2})")

    # (Optionnel) Débogage : afficher la pièce à destination avant de jouer
    try:
        piece_at_dest = game_instance.board.matrice[r2][c2]
        print(f"DEBUG: Contenu réel de la case d'arrivée ({r2}, {c2}): {piece_at_dest}")
    except (IndexError, TypeError):
        print("DEBUG: Coordonnées d'arrivée hors limites ou invalides.")

    # Exécution du coup
    result = game_instance.moves(r1, c1, r2, c2)
    print(f"Résultat de l'exécution: {result}")
    print(f"\nCouleur jouée: {game_instance.current_player}\nRésultat: {result}")
    
    return result

def execute_human_turn(game_instance: Game):
    """Exécute le tour du joueur humain."""
    print("\n--- C'EST À VOUS DE JOUER (NOIR) ---")
    
    move_input = input("Entrez votre coup (r1,c1,r2,c2): ")
    try:
        r1, c1, r2, c2 = map(int, move_input.split(','))
        result_black = game_instance.moves(r1, c1, r2, c2)
        print(f"Résultat du coup Noir: {result_black}")
    except ValueError:
        print("Entrée invalide. Le jeu doit être redémarré.")
    except IndexError:
         print("Coordonnées hors limites (0-9).")


if __name__ == "__main__":
    
    my_game = Game()
    ai_bot = DraughtsAI() # Crée et initialise la connexion Groq
    
    if ai_bot.client is None:
        print("Impossible de lancer le jeu sans connexion IA.")
        exit()

    print("--- Plateau Initial ---")
    print(my_game.board)
    print("-" * 25)

    # 1. Tour de l'IA (Blancs)
    if my_game.current_player == "White":
        execute_ai_turn(my_game, ai_bot)

    print("\n--- Plateau Après le Coup de l'IA (Blanc) ---")
    print(my_game.board)
    print("-" * 25)
    
    # 2. Tour de l'Humain (Noirs)
    if my_game.current_player == "Black":
        execute_human_turn(my_game)

    print("\n--- Plateau Après le Coup de l'Humain (Noir) ---")
    print(my_game.board)
    print(f"Prochain joueur : {'Blanc' if my_game.current_player == "White" else "Noir"}")

