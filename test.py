from game import Game, White, White_lady, Black

jeu = Game()

# On vide le plateau
jeu.board.matrice = [[0 for _ in range(10)] for _ in range(10)]

# Position dame blanche
jeu.board.matrice[4][4] = White_lady

# Position pion noir à capturer
jeu.board.matrice[6][2] = Black

print("\nPlateau avant capture :")
for ligne in jeu.board.matrice:
    print(ligne)

print("\nTest capture dame :")
print(jeu.moves(4, 4, 7, 1))   # <-- Bonne case d’atterrissage

print("\nPlateau après capture :")
for ligne in jeu.board.matrice:
    print(ligne)
