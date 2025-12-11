column={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
piece_dic={"pw":"White","dw":"White_lady","pb":"Black","db":"Black_lady","vw":"Vide_White","vb":"Vide_brown"}
inv_piece_dic={'White': 'pw', 'White_lady': 'dw', 'Black': 'pb', 'Black_lady': 'db', 'Vide_White': 'vw', 'Vide_brown': 'vb'}
white_positions = [(1,2),(3,2),(5,2),(7,2),(9,2),
        (2,1),(4,1),(6,1),(8,1),(10,1),
        (1,4),(3,4),(5,4),(7,4),(9,4),
        (2,3),(4,3),(6,3),(8,3),(10,3),
        (1,6),(3,6),(5,6),(7,6),(9,6),
        (2,5),(4,5),(6,5),(8,5),(10,5),
        (1,8),(3,8),(5,8),(7,8),(9,8),
        (2,7),(4,7),(6,7),(8,7),(10,7),
        (1,10),(3,10),(5,10),(7,10),(9,10),
        (2,9),(4,9),(6,9),(8,9),(10,9)
]
brown_positions = [(1,1),(3,1),(5,1),(7,1),(9,1),
        (2,2),(4,2),(6,2),(8,2),(10,2),
        (1,3),(3,3),(5,3),(7,3),(9,3),
        (2,4),(4,4),(6,4),(8,4),(10,4),
        (1,5),(3,5),(5,5),(7,5),(9,5),
        (2,6),(4,6),(6,6),(8,6),(10,6), 
        (1,7),(3,7),(5,7),(7,7),(9,7),
        (2,8),(4,8),(6,8),(8,8),(10,8),
        (1,9),(3,9),(5,9),(7,9),(9,9),
        (2,10),(4,10),(6,10),(8,10),(10,10)
]


class Board():
    def __init__(self):
        """self.matrice= [
            ["pb","vw","pb","vw","pb","vw","pb","vw","pb","vw"],\
            ["vw","pb","vw","pb","vw","pb","vw","pb","vw","pb"],\
            ["pb","vw","pb","vw","pb","vw","pb","vw","pb","vw"],\
            ["vw","pb","vw","pb","vw","pb","vw","pb","vw","pb"],\
            ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["pw","vw","pw","vw","pw","vw","pw","vw","pw","vw"],\
            ["vw","pw","vw","pw","vw","pw","vw","pw","vw","pw"],\
            ["pw","vw","pw","vw","pw","vw","pw","vw","pw","vw"],\
            ["vw","pw","vw","pw","vw","pw","vw","pw","vw","pw"]]"""#Matrice pour vrai jeu
        """self.matrice= [
            ["pb","vw","pb","vw","pb","vw","pb","vw","pb","vw"],\
            ["vw","pb","vw","pb","vw","pb","vw","pb","vw","pb"],\
            ["pb","vw","pb","vw","pb","vw","pb","vw","pb","vw"],\
            ["vw","pb","vw","pb","vw","pb","vw","pb","vw","pb"],\
            ["vb","vw","pw","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","pw","vw","pw","vw","pw","vw","pw","vw"],\
            ["vw","pw","vw","vb","vw","pw","vw","pw","vw","pw"],\
            ["pw","vw","pw","vw","pw","vw","pw","vw","pw","vw"],\
            ["vw","pw","vw","pw","vw","pw","vw","pw","vw","pw"]]"""#matrice test double capture
        self.matrice=["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","vb","vw","pw","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","pb","vw","vb","vw","vb","vw","vb"],\
            ["vb","vw","pw","vw","vb","vw","vb","vw","vb","vw"],\
            ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"]#matrice pour promotion et win
    def get_piece(self, r, c):
        return piece_dic[self.matrice[r][c]]

    def set_piece(self, r, c, value):
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
    def __init__(self):
        self.board = Board()
        self.current_player = "White"
        self.gagnant = None
        self.state = "Started"
    def is_started(self):
        return self.state=="Started"
    def switch_turn(self):  #Fonction pour changer de joueur 
        if self.current_player == "White":
            self.current_player = "Black"
        else:
            self.current_player = "White"

    def get_possible_captures(self, r, c): 
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
        piece = self.board.get_piece(r, c)

        # Un pion blanc devient une Dame
        if piece == "White" and r == 0:
            self.board.set_piece(r, c, "White_lady")

        # Un pion noir Devient une Dame
        if piece == "Black" and r == 9:
            self.board.set_piece(r, c, "Black_lady")


    def moves(self, r1, c1, r2, c2):
        
        board = self.board.matrice
        piece = piece_dic[board[r1][c1]]
      

        if piece in ("Vide_brown","Vide_white"):
            return "pas de pièce sur la case"
        
        if (piece in ("White", "White_lady") and self.current_player != "White") or (piece in ("Black", "Black_lady") and self.current_player != "Black"):
            return "Ce n'est pas à toi de jouer"
        
        if piece_dic[board[r2][c2]] not in ("Vide_brown","Vide_white"):
            return "La case d'arrivée n'est pas vide"

        dr = r2 - r1
        dc = c2 - c1

        #Déplacement standard"
        if abs(dr) == 1 and abs(dc) == 1: 

            if piece == "White" and dr != -1:
                return "Les pions blancs vont vers le haut du plateau sauf si vous êtes une dame"
            if piece == "Black" and dr != +1:
                return "Les pions noirs vont vers le bas du plateau sauf si vous êtes une dame"

            # Déplacements
            
            board[r1][c1] = "vw" if (r1,c1) in white_positions else "vb" #Case de la où l'on vient devient vide
            board[r2][c2] = inv_piece_dic.get(piece) # Nouvelle case occupée par le pion

            self.promote_if_needed(r2, c2)  # Si la case d'arrivée est une case du bout du plateau"

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
        
            board[r1][c1] = "vw" if (r1,c1) in white_positions else "vb" #Case de la où on vient devient vide
            board[mid_r][mid_c] = "vw" if (r1,c1) in white_positions else "vb" #SI l'on a manger un pion la case devient vide car le pion est retiré
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
                board[current_r][current_c] = "vw" if (r1,c1) in white_positions else "vb"
                board[eat_r][eat_c] = "vw" if (r1,c1) in white_positions else "vb"
                board[next_r][next_c] = inv_piece_dic.get(piece)

                current_r, current_c = next_r, next_c
                if not self.get_possible_captures(current_r, current_c):
                    break
                self.promote_if_needed(current_r, current_c)


            self.switch_turn() # passer à l'autre joueur

            return board
        else:
            return None
        
    import json

    def llm_move(self, groq_client, system_prompt):
        """Demande à l'IA (via Groq) un coup et l'exécute."""

        # 1. Vérification du client (pas besoin de global)
        if groq_client is None:
            print("Client Groq non initialisé. Impossible de demander le coup.")
            return "Échec de l'obtention du coup (Client Groq absent)"

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
                model="llama3-8b-8192", 
                messages=[
                    {"role": "system", "content": system_prompt}, 
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"} 
            )
            
            # ... (Le reste du code de parsing et d'exécution reste le même) ...
            response_text = response.choices[0].message.content
            move_data = json.loads(response_text)
            
            r1 = move_data.get('r1')
            c1 = move_data.get('c1')
            r2 = move_data.get('r2')
            c2 = move_data.get('c2')
            
            if not all(isinstance(coord, int) for coord in [r1, c1, r2, c2]):
                raise ValueError(f"Le format JSON de l'IA est incorrect ou incomplet: {response_text}")
    
            print(f"L'IA Groq suggère le coup : ({r1}, {c1}) -> ({r2}, {c2})")
            
            result = self.moves(r1, c1, r2, c2)
            
            print(f"Résultat de l'exécution: {result}")
            return result
        
        except Exception as e:
            print(f"Erreur lors de l'appel ou du traitement de l'IA Groq : {e}")
            return "Échec de l'obtention du coup de l'IA Groq"
        




    


