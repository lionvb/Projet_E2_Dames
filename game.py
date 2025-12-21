import json
#game.py
"""Fichier principal contenant la logique du jeu de dames:
-Les contenants du jeu
-La classe Board
-La classe game"""

#Matrice qui permet de transformer une colonne en index 
column={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
#dictionnaire reliant les codes internes aux type de pieces
 
#Dictionnaire reliant les codes internes aux types de pièces
piece_dic = {"pw":"White", # pion blanc
             "dw":"White_lady", # dame blanche
             "pb":"Black", # pion noir
             "db":"Black_lady", # dame noire
             "vw":"Vide_White", # case claire vide
             "vb":"Vide_brown" # case foncée vide
             }
# Dictionnaire inverse pour convertir un type de pièce en code interne
inv_piece_dic={'White': 'pw', 'White_lady': 'dw', 'Black': 'pb', 'Black_lady': 'db', 'Vide_White': 'vw', 'Vide_brown': 'vb'}
 
# cases blanches initiales 
white_positions = [(0,1),(2,1),(4,1),(6,1),(8,1),
        (1,0),(3,0),(5,0),(7,0),(9,0),
        (0,3),(2,3),(4,3),(6,3),(8,3),
        (1,2),(3,2),(5,2),(7,2),(9,2),
        (0,5),(2,5),(4,5),(6,5),(8,5),
        (1,4),(3,4),(5,4),(7,4),(9,4),
        (0,7),(2,7),(4,7),(6,7),(8,7),
        (1,6),(3,6),(5,6),(7,6),(9,6),
        (0,9),(2,9),(4,9),(6,9),(8,9),
        (1,8),(3,8),(5,8),(7,8),(9,8)
]
# brown_positions calculées 
brown_positions = [(r,c) for r in range(10) for c in range(10) if (r,c) not in white_positions]
 
 
class Board():
    """Classe représentant le plateau de jeu.
    Elle contient la matrice 10x10 et les méthodes d'accès aux pièces."""
    def __init__(self):
        """Initialise le plateau avec une configuration prédéfinie.
        Chaque case contient un code de pièce (pw, pb, vw, vb, etc.)."""
        self.matrice= [
            ["pb","vw","pb","vw","pb","vw","pb","vw","pb","vw"],\
            ["vw","pb","vw","pb","vw","pb","vw","pb","vw","pb"],\
            ["pb","vw","pb","vw","pb","vw","pb","vw","pb","vw"],\
            ["vw","pb","vw","pb","vw","pb","vw","pb","vw","pb"],\
            ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["pw","vw","pw","vw","pw","vw","pw","vw","pw","vw"],\
            ["vw","pw","vw","pw","vw","pw","vw","pw","vw","pw"],\
            ["pw","vw","pw","vw","pw","vw","pw","vw","pw","vw"],\
            ["vw","pw","vw","pw","vw","pw","vw","pw","vw","pw"]]#Matrice pour vrai jeu
        """self.matrice=[["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","vb","vw","pw","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","pb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","pw","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"]]"""#matrice pour promotion et win
    def get_piece(self, r, c):
        """Retourne le type de pièce (White, Black, White_lady, etc.)
        présente à la position (r, c)."""
        return piece_dic[self.matrice[r][c]]
 
    def set_piece(self, r, c, value):
        """Place une pièce donnée (value) à la position (r, c)
        en utilisant le dictionnaire inverse."""
        self.matrice[r][c] = inv_piece_dic[value]

    def __str__(self):
        # Mappage des codes internes aux symboles attendus par l'IA (W, Wl, B, Bl, .)
        mapping = {
            "pw": "W",
            "dw": "Wl",
            "pb": "B",
            "db": "Bl",
            "vw": ".", # Case vide blanche
            "vb": ".", # Case vide marron
        }
        
        board_str = ""
        # self.matrice est une liste de tuples ou de listes représentant les lignes
        for row in self.matrice:
            # Joindre les symboles, séparés par un espace
            board_str += " ".join(mapping.get(cell, '?') for cell in row)
            board_str += "\n"
            
        return board_str.strip() # Renvoie la chaîne de caractères formatée

class Game():
    """Classe principale gérant le déroulement de la partie :
    - tour du joueur
    - déplacements
    - promotions
    - captures"""
    def __init__(self):
        """Initialise une nouvelle partie :
        - plateau
        - joueur courant
        - état de la partie"""
        self.board = Board()
        self.current_player = "White"
        self.winner = None
        self.state = "Started"
 
    def is_started(self):
        """Indique si la partie est en cours."""
        return self.state == "Started"
 
    def switch_turn(self):
        """Change le joueur courant (White ↔ Black)."""
        if self.current_player == "White":
            self.current_player = "Black"
        else:
            self.current_player = "White"

    def blackwin(self,m):
        """Vérifie si le joueur noir a gagné
        (plus aucun pion blanc sur le plateau)."""
        for i in m:
            for j in i:
                if j=="pw"or j=="dw":
                    return False
        return True
    
    def whitewin(self,m):
        """Vérifie si le joueur blanc a gagné
        (plus aucun pion noir sur le plateau)."""
        for i in m:
            for j in i:
                if j=="pb"or j=="db":
                    return False
        return True
                    

    def get_empty_code(self, r, c):
        # Utilise l'indexation 1-10 pour vérifier si la position est 'white_positions'
        pos_1_10 = (r + 1, c + 1)
        # Si la position n'est ni blanche, ni marron (cas d'erreur), on suppose 'vb'
        if pos_1_10 in white_positions:
            return "vw"
        elif pos_1_10 in brown_positions:
            return "vb"
        # Pour les cases non jouables ou hors limite, nous retournons une couleur par défaut
        return "vb"
    

    def get_possible_captures(self, r, c): 
        """Calcule toutes les captures possibles pour une pièce
        située en (r, c).
        Retourne une liste de coups possibles."""
        print(r,c)
        # Va retourner toutes les captures possibles sous la forme
        # [(r_arrivée, c_arrivée, r_mangé, c_mangé), ...]
        # ex Atterrir en (4, 6) en mangeant la pièce en (3, 5)
        board = self.board.matrice
        piece = piece_dic[board[r][c]] # On regarde quelle type de pièce est sur la case
        moves = [] # Liste des captures
        

        if piece == "White_lady" or piece == "Black_lady":
            directions = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
        elif piece == "White":
            directions = [(-1, -1), (-1, +1)]
        else: # La piece == Black
            directions = [(+1, -1), (+1, +1)]

        for dr, dc in directions:
            # Position pièce ennemie -> case juste devant le pion
            enemy_r = r + dr
            enemy_c = c + dc
            # Position d'arrivée avec capture -> case située 2 cases plus loin
            jump_r = r + 2*dr
            jump_c = c + 2*dc
            #Vérif des limites du plateau
            if  not (0 <= enemy_r < 10 and 0 <= enemy_c < 10):
                continue
            if  not (0 <= jump_r < 10 and 0 <= jump_c < 10):
                continue

            enemy_piece = piece_dic[board[enemy_r][enemy_c]] # Position de la pièce ennemie

            # On vérifie que c'est bien un ennemi
            if piece in ("White", "White_lady") and enemy_piece not in ("Black", "Black_lady"):
                continue
            if piece in ("Black", "Black_lady") and enemy_piece not in ("White", "White_lady"):
                continue

            if board[jump_r][jump_c] not in ("Vide_brown","Vide_white"): # La case est libre
                continue
            
            moves.append((jump_r, jump_c, enemy_r, enemy_c))
        return moves

    def promote_if_needed(self, r, c):
        """Transforme un pion en dame si celui-ci atteint
        la dernière ligne adverse."""
        piece = self.board.get_piece(r, c)
        if piece == "White" and r == 0:
            self.board.set_piece(r, c, "White_lady")
        if piece == "Black" and r == 9:
            self.board.set_piece(r, c, "Black_lady")
 
    def get_possible_captures(self, r, c):
        """
        Retourne toutes les captures légales depuis (r,c).
        Format : [(landing_r, landing_c, eaten_r, eaten_c), ...]
        Règles :
         - pour un pion : case ennemie à (r+dr,c+dc) et atterrissage à (r+2dr,c+2dc)
         - pour une dame : on balaye chaque diagonale,
           on cherche la première pièce rencontrée ; si c'est un ennemi
           et la case immédiatement après est libre -> capture possible, landing = ennemi + (dr,dc)
           (=> la dame s'arrête **sur la case immédiatement après** l'ennemi)
        """
        board = self.board.matrice
        piece = piece_dic[board[r][c]]
        moves = []
 
        is_lady = piece in ("White_lady", "Black_lady")
        is_white = piece in ("White", "White_lady")
 
        directions = [(-1,-1), (-1,1), (1,-1), (1,1)]
 
        for dr, dc in directions:
            if not is_lady:
                # pion : capture simple en 2 cases
                enemy_r = r + dr
                enemy_c = c + dc
                landing_r = r + 2*dr
                landing_c = c + 2*dc
                #Vérif des limites du pkateau
                if not (0 <= enemy_r < 10 and 0 <= enemy_c < 10 and 0 <= landing_r < 10 and 0 <= landing_c < 10):
                    continue
 
                enemy_piece = piece_dic[board[enemy_r][enemy_c]]
                landing_piece = piece_dic[board[landing_r][landing_c]]
                #vérifie si la pièce adjacente est ennemie
                if is_white and enemy_piece not in ("Black", "Black_lady"):
                    continue
                if (not is_white) and enemy_piece not in ("White", "White_lady"):
                    continue
                #Vérfie si la case d'arrivée est vie
                if landing_piece in ("Vide_White", "Vide_brown"):
                    moves.append((landing_r, landing_c, enemy_r, enemy_c))
                continue
 
            # Dame : balayer la diagonale, trouver la PREMIERE pièce rencontrée.
            step_r = r + dr
            step_c = c + dc
            enemy_found = False
            enemy_r = enemy_c = None
 
            # on avance case par case jusqu'à sortir ou trouver un bloc
            while 0 <= step_r < 10 and 0 <= step_c < 10:
                p = piece_dic[board[step_r][step_c]]
                if p in ("Vide_brown", "Vide_White"):
                    # case vide : si on a déjà trouvé un ennemi, la première case vide
                    # immédiatement après l'ennemi est candidate (on ajoute et stop)
                    if enemy_found:
                        # landing = cette case vide directement après l'ennemi
                        moves.append((step_r, step_c, enemy_r, enemy_c))
                        break
                    # sinon on continue à avancer à la recherche d'une pièce
                    step_r += dr
                    step_c += dc
                    continue
 
                # si ici, case occupée
                if not enemy_found:
                    # si cette pièce est un ennemi -> marque-la et continue
                    if (is_white and p in ("Black", "Black_lady")) or (not is_white and p in ("White", "White_lady")):
                        enemy_found = True
                        enemy_r, enemy_c = step_r, step_c
                        # après avoir marqué l'ennemi, on doit regarder la case suivante
                        step_r += dr
                        step_c += dc
                        continue
                    else:
                        # si c'est une pièce amie ou obstacle -> pas de capture possible sur cette diagonale
                        break
                else:
                    # on a déjà trouvé un ennemi et sommes tombés sur une 2ème pièce (ami ou ennemi) -> stop
                    break
 
        return moves
 
    def moves(self, r1, c1, r2, c2):
        """
        Effectue un déplacement ou une capture (avec captures multiples automatiques).
        Renvoie :
         - la matrice (board) en cas de succès (pratique pour le bot),
         - une chaîne d'erreur si coup invalide.
        """
        board = self.board.matrice
        piece = piece_dic[board[r1][c1]]
        # Vérification des potentielles erreurs
        if piece in ("Vide_brown","Vide_White"):
            return "pas de pièce sur la case"
 
        if (piece in ("White", "White_lady") and self.current_player != "White") or \
           (piece in ("Black", "Black_lady") and self.current_player != "Black"):
            return "Ce n'est pas à toi de jouer"
 
        if piece_dic[board[r2][c2]] not in ("Vide_brown","Vide_White"):
            return "La case d'arrivée n'est pas vide"
        if self.winner!=None:
            return "La partie est finie, aucun mouvement peut être réalisé"

        is_lady = piece in ("White_lady", "Black_lady")
        is_white = piece in ("White", "White_lady")

        #Déplacement de la dame
        if is_lady:
            print("lady")
            dr = r2 - r1
            dc = c2 - c1
 
            # déplacement strictement diagonal
            if abs(dr) != abs(dc):
                return "Une dame se déplace uniquement en diagonale"
 
            step_r = 1 if dr > 0 else -1
            step_c = 1 if dc > 0 else -1
 
            cur_r = r1 + step_r
            cur_c = c1 + step_c
 
            captured = []
 
            while cur_r != r2 and cur_c != c2:
                p = piece_dic[board[cur_r][cur_c]]
 
                # pion allié → mouvement interdit
                if (is_white and p in ("White","White_lady")) or \
                (not is_white and p in ("Black","Black_lady")):
                    return "Une dame ne peut pas passer au-dessus d'un pion allié"
 
                # pion adverse → à capturer
                if (is_white and p in ("Black","Black_lady")) or \
                (not is_white and p in ("White","White_lady")):
                    captured.append((cur_r, cur_c))
 
                cur_r += step_r
                cur_c += step_c
 
            # --- appliquer le mouvement ---
            board[r1][c1] = "vw" if (r1, c1) in white_positions else "vb"
            board[r2][c2] = inv_piece_dic[piece]
 
            # supprimer tous les pions capturés
            for rr, cc in captured:
                board[rr][cc] = "vw" if (rr, cc) in white_positions else "vb"
            if self.blackwin(board):
                self.winner="Black"
                return "La partie est finie, aucun mouvement peut être réalisé"
            if self.whitewin(board):
                self.winner="White"
                return "La partie est finie, aucun mouvement peut être réalisé"
            self.switch_turn()
            return board

        #Déplacement d'un pion
        dr = r2 - r1
        dc = c2 - c1

        #Vérification des erreurs        
        if abs(dr) == 1 and abs(dc) == 1:
            if piece == "White" and dr != -1:
                return "Les pions blancs vont vers le haut du plateau sauf si vous êtes une dame"
            if piece == "Black" and dr != 1:
                return "Les pions noirs vont vers le bas du plateau sauf si vous êtes une dame"

            # Déplacements

            #board[r1][c1] = self.get_empty_code(r1, c1) 
            #board[r2][c2] = inv_piece_dic.get(piece)
            board[r1][c1] = "vw" if (r1,c1) in white_positions else "vb" #Case de la où l'on vient devient vide
            board[r2][c2] = inv_piece_dic.get(piece) # Nouvelle case occupée par le pion

            self.promote_if_needed(r2, c2)  # Si la case d'arrivée est une case du bout du plateau"
            if self.blackwin(board):
                self.winner="Black"
                return "La partie est finie, aucun mouvement peut être réalisé"
            if self.whitewin(board):
                self.winner="White"
                return "La partie est finie, aucun mouvement peut être réalisé"
            self.switch_turn() # passer à l'autre joueur

            return board
        
        # Déplacement avec capture d'un pion    
        if abs(dr) >= 2 or abs(dc) >= 2:  

            mid_r = (r1 + r2) // 2
            mid_c = (c1 + c2) // 2
            middle_piece = piece_dic[board[mid_r][mid_c]]

            if piece in ("White", "White_lady") and middle_piece not in ("Black", "Black_lady"):
                return "Pas de pièce à capturer"
            if piece in ("Black", "Black_lady") and middle_piece not in ("White", "White_lady"):
                return "Pas de pièce à capturer"

            board[r1][c1] = self.get_empty_code(r1, c1)
            board[mid_r][mid_c] = self.get_empty_code(mid_r, mid_c)
            #board[r1][c1] = "vw" if (r1,c1) in white_positions else "vb" #Case de la où on vient devient vide
            #board[mid_r][mid_c] = "vw" if (r1,c1) in white_positions else "vb" #SI l'on a manger un pion la case devient vide car le pion est retiré
            board[r2][c2] = inv_piece_dic.get(piece) # Nouvelle case occupé par le pion

            self.promote_if_needed(r2, c2)  # Si pendant que l'on mange on arrive au bout du board

            current_r, current_c = r2, c2
            #DOUBLE CAPTURE NE FONCTIONNE PAS IL FAUT RECTIFIER çA
            # Tant qu'une capture est possible on continue 
            while True:
                print(current_r,current_c)
                next_caps = self.get_possible_captures(current_r, current_c)
                
                if not next_caps: # Plus de capture possible
                    break

                #On peut choisir la première capture
                next_r, next_c, eat_r, eat_c = next_caps[0]

                #Exécution de la capture suivante
                board[current_r][current_c] = self.get_empty_code(current_r, current_c)
                board[eat_r][eat_c] = self.get_empty_code(eat_r, eat_c)
                #board[current_r][current_c] = "vw" if (r1,c1) in white_positions else "vb"
                #board[eat_r][eat_c] = "vw" if (r1,c1) in white_positions else "vb"
                board[next_r][next_c] = inv_piece_dic.get(piece)

                current_r, current_c = next_r, next_c
                if not self.get_possible_captures(current_r, current_c):
                    break
                self.promote_if_needed(current_r, current_c)
            if self.blackwin(board):
                self.winner="Black"
                return "La partie est finie, aucun mouvement peut être réalisé"
            if self.whitewin(board):
                self.winner="White"
                return "La partie est finie, aucun mouvement peut être réalisé" 
            self.switch_turn() # passer à l'autre joueur

            return board
        else:

            return ("Déplacement invalide")
     
    def print_board(self):
        """
        Affiche le plateau en version lisible (noms des pièces).
        """
        for row in self.board.matrice:
            print([piece_dic.get(cell, cell) for cell in row])

    def get_all_valid_moves(self, player_color):
        """Génère tous les coups possibles pour un joueur donné ("White" ou "Black").
        Retourne une liste de tuples : (r_start, c_start, r_end, c_end, is_capture)"""
        moves = []
        captures = []
        board = self.board.matrice
        
        # On détermine les directions de mouvement simples selon la couleur
        # Blanc monte (r diminue), Noir descend (r augmente)
        pion_direction = -1 if player_color == "White" else 1
        
        # Mapping pour identifier les pièces du joueur
        my_pieces = ["White", "White_lady"] if player_color == "White" else ["Black", "Black_lady"]
        
        for r in range(10):
            for c in range(10):
                p = piece_dic[board[r][c]]
                
                # Si ce n'est pas ma pièce, on passe
                if p not in my_pieces:
                    continue
                
                is_lady = "_lady" in p
                
                # 1. Regarder les CAPTURES (Prises)
                possible_caps = self.get_possible_captures(r, c)
                for cap in possible_caps:
                    # format cap: (landing_r, landing_c, eaten_r, eaten_c)
                    captures.append((r, c, cap[0], cap[1], True))
                
                # 2. Regarder les DÉPLACEMENTS SIMPLES
                # (Seulement si on n'est pas obligé de manger, mais on liste tout pour l'instant)
                directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
                
                for dr, dc in directions:
                    # Pour un pion, on vérifie qu'il va dans le bon sens (sauf dame)
                    if not is_lady:
                        if dr != pion_direction:
                            continue
                            
                    # Logique déplacement PION
                    if not is_lady:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < 10 and 0 <= nc < 10:
                            if piece_dic[board[nr][nc]] in ("Vide_brown", "Vide_White"):
                                moves.append((r, c, nr, nc, False))
                                
                    # Logique déplacement DAME
                    else:
                        step_r, step_c = r + dr, c + dc
                        while 0 <= step_r < 10 and 0 <= step_c < 10:
                            if piece_dic[board[step_r][step_c]] in ("Vide_brown", "Vide_White"):
                                moves.append((r, c, step_r, step_c, False))
                                step_r += dr
                                step_c += dc
                            else:
                                break # On est bloqué par une pièce
                                
        # RÈGLE DU JEU DE DAMES : La prise est souvent obligatoire.
        # Si des captures existent, on ne retourne que les captures.
        if captures:
            return captures
        return moves


    def llm_move(self, groq_client, system_prompt):
        """Demande à l'IA (via Groq) un coup et l'exécute."""

        # 1. Vérification du client (pas besoin de global)
        if groq_client is None:
            print("Client Groq non initialisé. Impossible de demander le coup.")
            return "Échec de l'obtention du coup (Client Groq absent)"
        if self.winner!=None:
            return "La partie est finie, aucun mouvement peut être réalisé"

        player_color = "Blanc (W/Wk)" if self.current_player == "White" else "Noir (B/Bk)"
        
        # Construction du USER PROMPT (état du jeu)
        user_prompt = (
            f"Le joueur actuel est : {player_color}. "
            "Voici la grille actuelle du plateau :\n"
            f"{str(self.board)}"
        )
        
        print(f"-> Consultation de l'IA Groq pour le joueur {player_color}...")
        
        try:
            # Appel à l'API Groq (utilisation de groq_client et system_prompt)
            response = groq_client.chat.completions.create(
                model="llama-3.1-8b-instant", 
                messages=[
                    {"role": "system", "content": system_prompt}, 
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"} 
            )
            
            # ... (Le reste du code de parsing et d'exécution reste le même) ...
            response_text = response.choices[0].message.content
            move_data = json.loads(response_text)
            r1 = int(move_data.get('r1'))
            c1 = int(move_data.get('c1'))
            r2 = int(move_data.get('r2'))
            c2 = int(move_data.get('c2'))
            
            if not all(isinstance(coord, int) for coord in [r1, c1, r2, c2]):
                raise ValueError(f"Le format JSON de l'IA est incorrect ou incomplet: {response_text}")
    
            print(f"L'IA Groq suggère le coup : ({r1}, {c1}) -> ({r2}, {c2})")

            try:
                piece_at_start=self.board.matrice[r1][c1]
                piece_at_dest = self.board.matrice[r2][c2]
                print(f"DEBUG: Contenu réel de la case d'arrivée ({r2}, {c2}): {piece_at_dest},{piece_at_start}")
            except (IndexError, TypeError):
                print("DEBUG: Coordonnées d'arrivée hors limites ou invalides.")
            
            #result = self.moves(r1, c1, r2, c2)
            
            #print(f"Résultat de l'exécution: {result}")
            return r1,c1,r2,c2
            
        
        except Exception as e:
            print(f"Erreur lors de l'appel ou du traitement de l'IA Groq : {e}")
            return "Échec de l'obtention du coup de l'IA Groq"
