- Langage : Python 3
- API : Groq 
- Format de données : JSON

- Prérequis :
    L'installation de la bibliothèque Groq est nécessaire.

- Description :
    la classe DraughtsBot se compose de deux parties majeures :
    1. L'initialisation (__init__) : Mise en place du client API en récupèrant automatiquement la clé d'API depuis les variables d'environnement et définition du prompt système contenant les règles métier.

    2. L'exécution (jouer_coup_ia) : Méthode faisant le pont entre l'instance du jeu et l'IA pour retourner le résultat du coup.



