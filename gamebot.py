import discord
import random
from discord import Embed
from discord.ext import commands
from game import Game,Board
from savegame import Partie_database

#Token bot discord
TOKEN = "MTQzODE5ODc0MTQ5NTU3ODY4NA.GDN8aq.A3Tl8m1bcVld2efrEctG6SGIjyvTXenwJAxGac"
# Définir les intentions
intents = discord.Intents.default()
intents.message_content = True
# Préfixe pour les commandes
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
active_games={}
jcj_queue=[]

emojis={"pw":"<:pion_blanc:1440245376673251348>","pb":"<:pion_noire:1440245418557706290>","dw":"<:dame_blanche:1440245260650287224>","db":"<:dame_noire:1440245307328958534>","vb":"<:vide_marron:1440255154837520415>","vw":":white_large_square:",
        "emoji1":"<:1_:1448707171805302855>","emoji2":"<:2_:1448707170538623060>","emoji3":"<:3_:1448707169406156851>","emoji4":"<:4_:1448707168244076614>","emoji5":"<:5_:1448707166033678398>","emoji6":"<:6_:1448707164532248719>","emoji7":"<:7_:1448707162309398680>","emoji8":"<:8_:1448707160027693077>","emoji9":"<:9_:1448707158198714369>","emoji10":"<:10:1448707157032702086>",
        "emojiA":"<:A_:1448707155221024998>","emojiB":"<:B_:1448707153501360269>","emojiC":"<:C_:1448707151999533156>","emojiD":"<:D_:1448707150221283379>","emojiE":"<:E_:1448707149147541676>","emojiF":"<:F_:1448707147671142549>","emojiG":"<:G_:1448707146198946047>","emojiH":"<:H_:1448707144865284226>","emojiI":"<:I_:1448707143439093821>","emojiJ":"<:J_:1448707142046449798>","videbleu":":blue_square:"}
Bordure_lettre=["vb","emojiA","emojiB","emojiC","emojiD","emojiE","emojiF","emojiG","emojiH","emojiI","emojiJ","vb"]
Bordure_chiffre=["emoji1","emoji2","emoji3","emoji4","emoji5","emoji6","emoji7","emoji8","emoji9","emoji10"]
lettretochiffre={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10}

def parse_move(txt):
    start,end=txt.split(":")
    return int(lettretochiffre[start[0].upper()])-1,int(start[1:])-1,int(lettretochiffre[end[0].upper()])-1,int(end[1:])-1

class GameSession:
    def __init__(self,game_instance,mode,players,difficulty=None):
        self.game=game_instance
        self.mode=mode
        self.players=players
        self.difficulty=difficulty
        self.database=Partie_database()

class ChoixAdversaire(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    async def start_game(self,interaction,mode,difficulty=None,player2=None):
        nouvelle_partie=Game()

        players={"White":interaction.user.id}
        if mode=="JCJ":
            players["Black"]=player2.id
            adversaire_name=player2.name
        else:
            players["Black"]=["IA"]
            adversaire_name=f"IA {difficulty}"
        active_games[interaction.channel_id]=GameSession(nouvelle_partie,mode,players,difficulty)
        embed = discord.Embed(title="Partie Lancée !", color=discord.Color.green())
        embed.add_field(name="White", value=interaction.user.name, inline=True)
        embed.add_field(name="Black", value=adversaire_name, inline=True)
        await interaction.channel.send(embed=embed)
        await display_board(interaction.channel, nouvelle_partie)

    @discord.ui.button(label="JCJ", style=discord.ButtonStyle.primary)
    async def JCJ_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        global jcj_queue
        if interaction.user in jcj_queue:
            return await interaction.response.send_message("Tu attends déjà un adversaire !", ephemeral=True)
        jcj_queue.append(interaction.user)
        if len(jcj_queue)>=2:
            p1=jcj_queue.pop(0)
            p2=p1=jcj_queue.pop(0)
            for item in self.children: item.disable=True
            await interaction.response.edit_message(view=self)
            await self.start_game(interaction,"JCJ",player2=p1)
        else:
            await interaction.response.send_message(f"{interaction.user.name} attend un adversaire ...",ephemeral=False)

    @discord.ui.button(label="IA facile", style=discord.ButtonStyle.primary)
    async def ia_facile(self, interaction: discord.Interaction, button: discord.ui.Button):
        for item in self.children:
                item.disabled = True
        await interaction.response.edit_message(view=self)
        await self.start_game(interaction, "IA", difficulty="facile")
        
    @discord.ui.button(label="IA LLM moyen", style=discord.ButtonStyle.primary)
    async def ia_llm(self, interaction: discord.Interaction, button: discord.ui.Button):
        for item in self.children:
                item.disabled = True
        await interaction.response.edit_message(view=self)
        await self.start_game(interaction, "IA", difficulty="moyen")

    @discord.ui.button(label="IA difficile", style=discord.ButtonStyle.primary)
    async def ia_difficile(self, interaction: discord.Interaction, button: discord.ui.Button):
        for item in self.children:
                item.disabled = True
        await interaction.response.edit_message(view=self)
        await self.start_game(interaction, "IA", difficulty="difficile")        

def embed_aff(msg,player_tour,player_tour_name):
    embed = Embed(title="Plateau de jeu", description=msg)
    embed.add_field(
        name="Au tour de : ",
        value=f" {player_tour_name} ({player_tour})",
    inline=False
    )
    return embed

async def display_board(channel, game_instance):
    plateau_mat = game_instance.board.matrice
    msg = "".join(emojis[x] for x in Bordure_lettre) + "\n"
    for a, ligne in enumerate(plateau_mat):
        msg += emojis[Bordure_chiffre[a]]
        msg += "".join(emojis[j] for j in ligne)
        msg += emojis[Bordure_chiffre[a]] + "\n"
    msg += "".join(emojis[x] for x in Bordure_lettre)
    couleur_actuelle = game_instance.current_player
    embed=Embed(title="Plateau de jeu", description=msg, color=discord.Color.blue())
    embed.add_field(name="Au tour de : ",value=f"{couleur_actuelle}",inline=False)
    await channel.send(embed=embed)
   
@bot.command()
async def dames(ctx):
    embed = discord.Embed(title="Jeu de Dames", description="Choisissez votre adversaire :")
    await ctx.send(embed=embed, view=ChoixAdversaire())

async def play_ai_turn(channel, session):
    """Gère le tour de l'IA"""
    game = session.game
    difficulty = session.difficulty
    possibility = game.get_all_valid_moves("Black")
    if not possibility:
        await channel.send("L'IA est bloquée ! Vous avez gagné ?")
        return
    move_tuple = random.choice(possibility)
    r1, c1, r2, c2, _ = move_tuple
    try:
        game.moves(r1, c1, r2, c2)
        
        # 5. On affiche le message et le plateau
        await channel.send(f"L'IA a joué : {r1},{c1} vers {r2},{c2}")
        
        # (Assure-toi d'avoir importé display_board ou qu'elle soit accessible)
        await display_board(channel, game)

    except Exception as e:
        print(f"Erreur IA : {e}")
        await channel.send("l'IA a essayé un coup interdit.")

@bot.command()
async def move(ctx,*,txt:str):
    #verif si une partie est active dans le salon
    session=active_games.get(ctx.channel.id)
    if not session:
        return await ctx.send("Aucune partie en cours ici ! Lancez avec `!dames`")
    game=session.game
    #verif le tour de l'utilisateur
    current_color=game.current_player
    expected_player_id=session.players.get(current_color)
    # verif si tour IA
    if expected_player_id=="IA":
        return await ctx.send(f"Attendez, c'est au tour de l'IA ({current_color}) !")
    if  expected_player_id!=ctx.author.id:
        return await ctx.send(f"Ce n'est pas votre tour ! C'est aux {current_color}s de jouer.")
    coords=parse_move(txt)
    if not coords:
        return await ctx.send("Format invalide ! Utilisez `!move A3:B4`")
    r1,c1,r2,c2=coords

    try:
        game.moves(c1,r1,c2,r2)
        session.database.coups(txt)
        await display_board(ctx.channel,game)
        if session.mode=="IA":
            await play_ai_turn(ctx.channel, session)
    except Exception as e:
        await ctx.send(f"Coup impossible : {e}")

@bot.command()
async def finish(ctx):
    session=active_games.get(ctx.channel.id)
    if session:
        session.database.dict()
        session.database.add_data()
        del active_games[ctx.channel.id] # On supprime la partie
        await ctx.send("Partie sauvegardée et terminée.")
    else: await ctx.send("Pas de partie à finir")

bot.run(TOKEN)