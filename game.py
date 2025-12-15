column={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
piece_dic={"pw":"White","dw":"White_lady","pb":"Black","db":"Black_lady","vw":"Vide_White","vb":"Vide_brown"}
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
    def __init__(self):
        # position de départ standard
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
        """self.matrice=["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","vb","vw","pw","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","pb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","pw","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"]"""#matrice pour promotion et win
    def get_piece(self, r, c):
        return piece_dic[self.matrice[r][c]]
 
    def set_piece(self, r, c, value):
        # value attendu : "White", "Black", "White_lady", "Black_lady", "Vide_White" ou "Vide_brown"
        self.matrice[r][c] = inv_piece_dic[value]
 
 
class Game():
    def __init__(self):
        self.board = Board()
        self.current_player = "White"
        self.gagnant = None
        self.state = "Started"
 
    def is_started(self):
        return self.state == "Started"
 
    def switch_turn(self):
        if self.current_player == "White":
            self.current_player = "Black"
        else:
            self.current_player = "White"
 
    def promote_if_needed(self, r, c):
        """Promotion automatique"""
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
 
                if not (0 <= enemy_r < 10 and 0 <= enemy_c < 10 and 0 <= landing_r < 10 and 0 <= landing_c < 10):
                    continue
 
                enemy_piece = piece_dic[board[enemy_r][enemy_c]]
                landing_piece = piece_dic[board[landing_r][landing_c]]
 
                if is_white and enemy_piece not in ("Black", "Black_lady"):
                    continue
                if (not is_white) and enemy_piece not in ("White", "White_lady"):
                    continue
 
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
 
        # validations de base
        if piece in ("Vide_brown","Vide_White"):
            return "pas de pièce sur la case"
 
        if (piece in ("White", "White_lady") and self.current_player != "White") or \
           (piece in ("Black", "Black_lady") and self.current_player != "Black"):
            return "Ce n'est pas à toi de jouer"
 
        if piece_dic[board[r2][c2]] not in ("Vide_brown","Vide_White"):
            return "La case d'arrivée n'est pas vide"
 
        dr = r2 - r1
        dc = c2 - c1
 
        # --- déplacement simple (1 diag)
        if abs(dr) == 1 and abs(dc) == 1:
            if piece == "White" and dr != -1:
                return "Les pions blancs vont vers le haut du plateau sauf si vous êtes une dame"
            if piece == "Black" and dr != 1:
                return "Les pions noirs vont vers le bas du plateau sauf si vous êtes une dame"
 
            board[r1][c1] = "vw" if (r1,c1) in white_positions else "vb"
            board[r2][c2] = inv_piece_dic.get(piece)
            self.promote_if_needed(r2, c2)
            self.switch_turn()
            return board
 
        # --- capture (pion ou dame)
        possible_caps = self.get_possible_captures(r1, c1)
 
        # vérifier si (r2,c2) est une capture légale
        chosen_cap = None
        for cap in possible_caps:
            if cap[0] == r2 and cap[1] == c2:
                chosen_cap = cap
                break
        if chosen_cap is None:
            return "Le déplacement n'est pas autorisé"
 
        # exécuter la capture choisie
        jump_r, jump_c, eat_r, eat_c = chosen_cap
 
        # vider départ, supprimer mangé, poser pièce
        board[r1][c1] = "vw" if (r1,c1) in white_positions else "vb"
        board[eat_r][eat_c] = "vw" if (eat_r,eat_c) in white_positions else "vb"
        board[jump_r][jump_c] = inv_piece_dic.get(piece)
 
        # promotion si besoin (pion qui arrive)
        self.promote_if_needed(jump_r, jump_c)
 
        # capture multiple automatique : on vérifie à partir de la nouvelle position
        cur_r, cur_c = jump_r, jump_c
        while True:
            next_caps = self.get_possible_captures(cur_r, cur_c)
            if not next_caps:
                break
            # on prend la première capture trouvée (tu peux remplacer par choix du joueur si souhaité)
            next_r, next_c, eat_r, eat_c = next_caps[0]
            board[cur_r][cur_c] = "vw" if (cur_r,cur_c) in white_positions else "vb"
            board[eat_r][eat_c] = "vw" if (eat_r,eat_c) in white_positions else "vb"
            board[next_r][next_c] = inv_piece_dic.get(piece)
            cur_r, cur_c = next_r, next_c
            self.promote_if_needed(cur_r, cur_c)
 
        self.switch_turn()
        return board
    
    def get_all_valid_moves(self, player_color):
        """
        Génère tous les coups possibles pour un joueur donné ("White" ou "Black").
        Retourne une liste de tuples : (r_start, c_start, r_end, c_end, is_capture)
        """
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