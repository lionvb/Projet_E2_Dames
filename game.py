

class Piece():
    def __init__(self, couleur, pion, dame):
        self.couleur = couleur
        self.est_dame = est_dame


class Grille():
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def __dimension__(self):
        return self.longueur * self.largeur

    def __affichage__(self):
        return f"La longueur est : {self.longueur} et la largeur est : {self.largeur}"


White = 1
White_lady = 2
Black = 3
Black_lady = 4

class Board():
    def __init__(self):
        self.matrice = [
            [3, 0, 3, 0, 3, 0, 3, 0, 3, 0],
            [0, 3, 0, 3, 0, 3, 0, 3, 0, 3],
            [3, 0, 3, 0, 3, 0, 3, 0, 3, 0],
            [0, 3, 0, 3, 0, 3, 0, 3, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        ]

    def get_piece(self, r, c):
        return self.matrice[r][c]

    def set_piece(self, r, c, value):
        self.matrice[r][c] = value


class Game():
    def __init__(self):
        self.board = Board()
        self.current_player = White
        self.gagnant = None

    def switch_turn(self):  #Fonction pour changer de joueur 
        if self.current_player == White:
            self.current_player = Black
        else:
            self.current_player = White

    def get_possible_captures(self, r, c): 
        # Va retourner toutes les captures possibles sous la forme
        # [(r_arrivée, c_arrivée, r_mangé, c_mangé), ...]
        # ex Atterrir en (4, 6) en mangeant la pièce en (3, 5)
        piece = self.board.get_piece(r, c) # On regarde quelle type de pièce est sur la case
        moves = [] # Liste des captures
        board = self.board.matrice

        if piece == White_lady or piece == Black_lady:
            directions = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
        elif piece == White:
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

            if  not (0 <= enemy_r < 10 and 0 <= enemy_c < 10):
                continue
            if  not (0 <= jump_r < 10 and 0 <= jump_c < 10):
                continue

            enemy_piece = board[enemy_r][enemy_c] # Position de la pièce ennemie

            # On vérifie que c'est bien un ennemi
            if piece in (White, White_lady) and enemy_piece not in (Black, Black_lady):
                continue
            if piece in (Black, Black_lady) and enemy_piece not in (White, White_lady):
                continue

            if board[jump_r][jump_c] != 0: # La case est libre
                continue
            
            moves.append((jump_r, jump_c, enemy_r, enemy_c))
        return moves

    def promote_if_needed(self, r, c):
        piece = self.board.get_piece(r, c)

        # Un pion blanc devient une Dame
        if piece == White and r == 0:
            self.board.set_piece(r, c, White_lady)

        # Un pion noir Devient une Dame
        if piece == Black and r == 9:
            self.board.set_piece(r, c, Black_lady)


    def moves(self, r1, c1, r2, c2):
        
        board = self.board.matrice
        piece = board[r1][c1]

        if piece == 0:
            return "pas de pièce sur la case"
        
        if (piece in (White, White_lady) and self.current_player != White) or (piece in (Black, Black_lady) and self.current_player != Black):
            return "Ce n'est pas à toi de jouer"

        if board[r2][c2] != 0:
            return "La case d'arrivée n'est pas vide"

        dr = r2 - r1
        dc = c2 - c1

        #Déplacement standart"
        if abs(dr) == 1 and abs(dc) == 1: 

            if piece == White and dr != -1:
                return "Les pions blancs vont vers le haut du plateau sauf si vous êtes une dame"
            if piece == Black and dr != +1:
                return "Les pions noirs vont vers le bas du plateau sauf si vous êtes une dame"

            # Déplacements
            board[r1][c1] = 0 #Case de la où on vient devient vide
            board[r2][c2] = piece # Nouvelle case occupé par le pion

            self.promote_if_needed(r2, c2)  # Si la case d'arrivée est une case du bout du plateau"

            self.switch_turn() # passer à l'autre joueur

            return "Déplacement effectué"

        # Déplacement avec capture d'un pion    
        if abs(dr) == 2 and abs(dc) == 2:  

            mid_r = (r1 + r2) // 2
            mid_c = (c1 + c2) // 2
            middle_piece = board[mid_r][mid_c]

            if piece in (White, White_lady) and middle_piece not in (Black, Black_lady):
                return "Pas de pièce à capturer"
            if piece in (Black, Black_lady) and middle_piece not in (White, White_lady):
                return "Pas de pièce à capturer"
        
            board[r1][c1] = 0 #Case de la où on vient devient vide
            board[mid_r][mid_c] = 0 #SI l'on a manger un pion la case devient vide car le pion est retiré
            board[r2][c2] = piece # Nouvelle case occupé par le pion

            self.promote_if_needed(r2, c2)  # Si pendant que l'on mange on arrive au bout du board

            current_r, current_c = r2, c2

            # Tant qu'une capture est possible on continue
            while True:
                next_caps = self.get_possible_captures(current_r, current_c)

                if not next_caps: # Plus de capture possible
                    break

                #On peut choisir la première capture
                next_r, next_c, eat_r, eat_c = next_caps[0]

                #Exécution de la capture suivante
                board[current_r][current_c] = 0
                board[eat_r][eat_c] = 0
                board[next_r][next_c] = piece

                current_r, current_c = next_r, next_c

                self.promote_if_needed(current_r, current_c)


            self.switch_turn() # passer à l'autre joueur

            return "Capture effectuée"
        else:
            return "Le déplacement n'est pas autorisé"


        






    


