Jeu de DAMES avec Discord

TUTO INSTALLATION :
 -Installer les dépendances
 Pour installer les modules et pouvoir les utiliser avec le code.

    1 Créer un environnment virtuel

    python -m venv <name>

    Remplacez <name> par le nom que vous souhaitez donner à votre environnement virtuel. Selon votre installation de Python, vous devrez peut-être utiliser python3 ou py au lieu de python.

    2 Activer l'environnement virtuel

    .\<name>\Scripts\activate

    Lorsque l'environnement virtuel est activé, vous devriez voir le nom de l'environnement en début de ligne dans votre terminal.

    3 Installer les dépendances

    Tapez : pip install -r requirements.txt

    Cela installera toutes les bibliothèques Python listées dans le fichier requirements.txt dont vous aurez besoin pour déployer le bot de jeu de dames.

-RECUP CLE API
 groq.com

 -RECUP VOTRE CLE DISCORD
    1) Aller sur le site web : [text](https://discord.com/developers/applications)
    
    2) Cliquer sur "New application", Donnez lui un nom et cliquez sur create

    3) Cliquez sur bot sur le coté gauche puis add bot et confirmez

    4) Puis cliquez sur reset Token et copiez le 

    5) Dans le terminal : set DISCORD_TOKEN=VOTRE_TOKEN_ICI pour y acceder sans le mettre en clair
    
    6) Donnez les permissions au bot:
       Allez dans "OAuth2" puis "URL Generator"
       Dans "Scopes" : cochez "bot"
       Et dans "bot permissions" cochez: "send messages","read message history", "Message Content Intent"

    7) Copiez le lien du bot et collez le sur google puis choisissez votre serveur où vous êtes administrateur

 -LANCEMENT BOT DISCORD
  Dans l'environnment précedemment crée et tapez la commande : 
    python gamebot.py
    Selon votre installation de Python, vous devrez peut-être utiliser python3 ou py au lieu de python.


COMMENT JOUER:
Entrez la commande !dames dans le chat discord
Un choix va s'afficher sur discord , il vous faudra choisir le mode de jeu que vous voulez.
Pour cela, cliquez sur la difficulté qui vous intéresse.
Ensuite le jeu de dames va s'afficher. 
Faites !move (case de départ):(case d'arrivée) (de la forme !mvoe A3:B4)
Et si vous voulez arretez une partie commencez mais mettre la partie sur la database, envoyer dasns le tchat !finish.

EXPLICATION DU CODE:
 -Fichier bot_llm_moyen_py
    - API : Groq (Modèle de langage haute performance)
    - Format de données : JSON

    - Prérequis :
        L'installation de la bibliothèque Groq est nécessaire.

    - Description :
        la classe DraughtsBot se compose de deux parties majeures :
        1. L'initialisation (__init__) : Mise en place du client API en récupèrant automatiquement la clé d'API depuis les variables d'environnement et définition du prompt système contenant les règles métier.

        2. L'exécution (jouer_coup_ia) : Méthode faisant le pont entre l'instance du jeu et l'IA pour retourner le résultat du coup.
 -Fichier Game.py
 -Fichier Gamebot.py
 -Fichier Savegame.py


REPARTITION DU TRAVAIL
Arthur
Nils
Victor
