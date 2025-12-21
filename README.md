Jeu de DAMES avec Discord

TUTO INSTALLATION :
 
    Pour installer les modules et pouvoir les utiliser avec le code.

    1. Créer un environnment virtuel

    python -m venv <name>

    Remplacez <name> par le nom que vous souhaitez donner à votre environnement virtuel. 
    Selon votre installation de Python, vous devrez peut-être utiliser python3 ou py au lieu de python.

    2. Activer l'environnement virtuel

    .\<name>\Scripts\activate

    Lorsque l'environnement virtuel est activé, vous devriez voir le nom de l'environnement en début de ligne dans votre terminal.

    3. Installer les dépendances

    Tapez : pip install -r requirements.txt

    Cela installera toutes les bibliothèques Python listées dans le fichier requirements.txt dont vous aurez besoin pour déployer le bot de jeu de dames.


-RECUP CLE API :
    
    Créer une clé API :
    1. Se rendre sur : [Groq cloud](https://console.groq.com/keys)
    2. se connecter et cliquer sur le bouton "Créer une clé API"
    3. Lui donner un nom 
    4. Stocker la clé crée pour y acceder sans le mettre en clair:
    set GROQ_API_KEY=key    
 


 -RECUP VOTRE CLE DISCORD
    
    1) Aller sur le site web : [Discord developpers](https://discord.com/developers/applications)
    
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

  -Pour l'affichage si vous n'utilisez pas notre token discord, il est fort probable que vous n'ayez pas les emojis.
  Vous pourrez les trouvez dans le dossier piece dames et les ajouter en important le dossier sur l'espace developpeur de Discord dans emoji sur la gauche.
  Ensuite il vous faudra remplacer dans le Programme gamebot.py(l.23) toute lesanciennes id par les nouvelles id qui vous seront données après l'importation


COMMENT JOUER:
Entrez la commande !dames dans le chat discord
Un choix va s'afficher sur discord , il vous faudra choisir le mode de jeu que vous voulez.
Pour cela, cliquez sur la difficulté qui vous intéresse.
Ensuite le jeu de dames va s'afficher. 
Faites !move (case de départ):(case d'arrivée) (de la forme !mvoe A3:B4)
Et si vous voulez arretez une partie commencez mais mettre la partie sur la database, envoyer dasns le tchat !finish.
Ainsi que !helps pour toute question


EXPLICATION DU CODE:
 
   -Fichier bot_llm_moyen_py
    
    - API : Groq
    - Format de données : JSON

    - Prérequis :
        L'installation de la bibliothèque Groq est nécessaire.

    - Description :
        la classe DraughtsBot se compose de deux parties majeures :
        1. L'initialisation (__init__) : Mise en place du client API en récupèrant automatiquement la clé d'API depuis les variables d'environnement et définition du prompt système contenant les règles métier.

        2. L'exécution (jouer_coup_ia) : Méthode faisant le pont entre l'instance du jeu et l'IA pour retourner le résultat du coup.


    -Fichier Game.py
      -Structure du Code:
         Plateau de jeu : Représenté par une matrice 10x10, chaque case contient des pièces (pions blancs, pions noirs, dames, ou cases vides).
         Classe Board : Gère l'état du plateau et permet d'accéder aux pièces avec des méthodes comme get_piece() et set_piece().
         Classe Game : Gère la logique du jeu : changement de tour, déplacements, captures, promotion des pions en dames, et vérification de la victoire.
         IA : Utilise un modèle de langage pour suggérer des coups via la méthode llm_move().
        
      -Fonctionnalités Clés:
         Déplacements des pièces selon les règles classiques des dames.
         Captures obligatoires et multiples.
         Promotion des pions en dames.
         Détection du gagnant (lorsqu'un joueur n'a plus de pions).

 -Fichier Gamebot.py
       - Commandes principales :
           !dames : Lance une partie et permet de choisir l'adversaire.
           !move A3:B4 : Effectue un mouvement sur le plateau (format : !move [Départ][Arrivée]).
           !finish : Sauvegarde et termine la partie.
           !helps : Affiche les instructions de base pour jouer.
        
       - Modes de jeu :
           JCJ : Deux joueurs humains jouent l'un contre l'autre.
           IA Facile : Affrontez une IA qui fait des mouvements aléatoires.
           IA Moyen (LLM) : Affrontez une IA plus avancée utilisant un modèle de langage (LLM) pour décider de ses coups.
        
       - Comportement du jeu :
          Le jeu vérifie à chaque tour si c'est au tour du joueur, et vous avertit si ce n'est pas votre tour.
          Les joueurs peuvent jouer avec une IA ou avec d'autres joueurs en ligne via Discord.
          L'IA "facile" joue aléatoirement, tandis que l'IA "moyenne" utilise une logique de mouvement avancée.
        
       - Structures principales :
            GameSession : Gère l'état de la partie en cours, y compris le mode (JCJ ou IA) et les joueurs.
            ChoixAdversaire : Interface utilisateur avec des boutons pour choisir le type d'adversaire (JCJ, IA Facile, IA Moyen).
            DraughtsBot : L'IA qui utilise un modèle de langage pour jouer intelligemment contre un joueur.

 -Fichier Savegame.py
    
    - Prérequis :
        L'installation de la bibliothèque pymongo est nécessaire.
    -Rôle:
        Le fichier Savegame.py gère la sauvegarde des parties de jeu de dames dans une base de données MongoDB hébergée en ligne.
        Il permet de conserver les informations importantes d’une partie : joueurs, coups joués, nombre de coups et vainqueur.
        Description de la classe Partie_database

        La classe Partie_database permet d’interagir avec la base de données.

        Initialisation (__init__)
        Connexion à la base MongoDB, création ou accès à la base Jeu_de_dames et à la collection Games.
        Une nouvelle partie est automatiquement numérotée et les variables de stockage sont initialisées.

        coups:
        Ajoute un coup joué à l’historique et incrémente le nombre total de coups.

        winner:
        Définit le vainqueur de la partie une fois celle-ci terminée.

        dict:
        Regroupe toutes les informations de la partie dans un dictionnaire prêt à être envoyé à la base de données.

        add_data:
        Enregistre définitivement la partie dans MongoDB.

        Conclusion
        Ce fichier permet d’assurer la persistance des données du jeu en stockant les parties jouées, ce qui facilite le suivi et l’analyse des parties.


REPARTITION DU TRAVAIL
   
   
   Arthur – Développement du moteur du jeu de dames (Intégralité du code du jeu de dame)
    
   - L’implémentation complète des règles officielles du jeu de dames
      - Déplacements des pions
      - Prises simples et multiples
      - Gestion des dames
      - Conditions de victoire et de fin de partie
   - La gestion de l’état du plateau et des tours de jeu
   - La validation des coups joués (coups légaux / illégaux)
   - La création d’une base solide permettant l’intégration du jeu sur d’autres plateformes (comme Discord)
    
    
   Victor – Intégration Discord et base de données
    
   - Le développement du bot Discord permettant de jouer au jeu de dames directement sur un serveur
   - La gestion des commandes Discord (création de partie, jouer un coup, affichage du plateau, etc.)
   - L’intégration de MongoDB pour :
      - Sauvegarder les parties en cours
      - Stocker les joueurs et leurs statistiques
      - Permettre la reprise des parties
   - La liaison entre le moteur du jeu et l’interface Discord
    
    
   Nils – Algorithme de requêtes basé sur un LLM (Niveau moyen)
    
   - La conception d’un algorithme capable de formuler et gérer des requêtes
   - L’utilisation d’un modèle de langage (LLM) pour analyser ou générer des réponses adaptées
   - L’intégration de cet algorithme dans le projet afin d’apporter une dimension intelligente (aide, analyse ou interaction avancée)
   - L’optimisation des requêtes pour obtenir des réponses cohérentes et exploitables
