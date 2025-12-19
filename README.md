Description :
Ce projet a été réalisé dans le cadre d'un développement visant à intégrer des modèles de langage (LLM) au sein d'un moteur de jeu de dames internationales (plateau 10x10). L'objectif est de permettre à une intelligence artificielle, via l'API Groq, de se comporter comme un joueur expert en analysant l'état du jeu et en proposant des coups stratégiques valides.

Langage : Python 3
API : Groq (Modèle de langage haute performance)
Format de données : JSON

la classe DraughtsBot :

Initialisation (__init__) : Mise en place du client API et définition du prompt système contenant les règles métier.

Exécution (jouer_coup_ia) : Méthode faisant le pont entre l'instance du jeu et l'IA pour retourner le résultat du coup.

Prérequis :
L'installation de la bibliothèque Groq est nécessaire

Configuration :
Le script récupère automatiquement la clé d'API depuis les variables d'environnement