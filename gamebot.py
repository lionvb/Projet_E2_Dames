import discord
from discord.ext import commands
from game import Game,Board

#Token bot discord
TOKEN = "MTQzODE5ODc0MTQ5NTU3ODY4NA.GDN8aq.A3Tl8m1bcVld2efrEctG6SGIjyvTXenwJAxGac"
# Définir les intentions (pour que ton bot voie les messages)
intents = discord.Intents.default()
intents.message_content = True
# Préfixe pour les commandes
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

PION_WHITE = "<:pion_blanc:1440245376673251348>";PION_BLACK = "<:pion_noire:1440245418557706290>";DAME_WHITE="<:dame_blanche:1440245260650287224>";DAME_BLACK="<:dame_noire:1440245307328958534>";VIDE_BROWN="<:vide_marron:1440255154837520415>";VIDE_WHITE=":white_large_square:"
emojis={None:DAME_BLACK,"pw":PION_WHITE,"pb":PION_BLACK,"dw":DAME_WHITE,"db":DAME_BLACK,"vb":VIDE_BROWN,"vw":VIDE_WHITE,"emoji1":":one:","emoji2":":two:","emoji3":":three:","emoji4":":four:","emoji5":":five:","emoji6":":six:","emoji7":":seven:","emoji8":":eight:","emoji9":":nine:","emoji10":":keycap_ten:","emojiA":":regional_indicator_a:","emojiB":":regional_indicator_b:","emojiC":":regional_indicator_c:","emojiD":":regional_indicator_d:","emojiE":":regional_indicator_e:","emojiF":":regional_indicator_f:","emojiG":":regional_indicator_g:","emojiH":":regional_indicator_h:","emojiI":":regional_indicator_i:","emojiJ":":regional_indicator_j:","videbleu":":blue_square:","L":":regional_indicator_l:"}
Bordure_lettre=["videbleu","emojiA","emojiB","emojiC","emojiD","emojiE","emojiF","emojiG","emojiH","emojiI","emojiJ","videbleu"]
Bordure_chiffre=["emoji1","emoji2","emoji3","emoji4","emoji5","emoji6","emoji7","emoji8","emoji9","emoji10"]
lettretochiffre={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10}

def parse_move(txt):
    start,end=txt.split(":")
    return int(lettretochiffre[start[0].upper()])-1,int(start[1:])-1,int(lettretochiffre[end[0].upper()])-1,int(end[1:])-1

@bot.command()
async def affich_mat(ctx,plateau_mat):
    await ctx.send("".join(emojis[x] for x in Bordure_lettre))
    a=0
    for i in plateau_mat:
            print(i)
            msg =emojis[Bordure_chiffre[a]]+ "".join(emojis[j] for j in i)+emojis[Bordure_chiffre[a]]
            print(msg)
            await ctx.send(msg)
            a+=1
    await ctx.send("".join(emojis[x] for x in Bordure_lettre))

@bot.command()
async def start(ctx):
    global jeu
    jeu=Game()
    plateau_mat=jeu.board.matrice
    await bot.get_command("affich_mat").callback(ctx, plateau_mat)
    await ctx.send("Vous êtes blanc, quel mouvement voulez vous faire? ")
    

@bot.command()
async def move(ctx,*,txt: str):
    if not jeu.is_started():
        await ctx.send("Il faut démarrer le jeu avec la commande `!start` avant de pouvoir bouger un pion !")
    else:
        r1,c1,r2,c2=parse_move(txt)
        print(r1,c1,r2,c2)
        plateau_mat=jeu.moves(c1,r1,c2,r2)
        print("hellofghfgh")
        print(plateau_mat)
        await bot.get_command("affich_mat").callback(ctx, plateau_mat)
    

"""plateau_mat = [
    ["pb","vw","pb","vw","pb","vw","pb","vw","pb","vw"],\
    ["vw","pb","vw","pb","vw","pb","vw","pb","vw","pb"],\
    ["pb","vw","pb","vw","pb","vw","pb","vw","pb","vw"],\
    ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
    ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
    ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
    ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
    ["vw","pw","vw","pw","vw","pw","vw","pw","vw","pw"],\
    ["pw","vw","pw","vw","pw","vw","pw","vw","pw","vw"],\
    ["vw","pw","vw","pw","vw","pw","vw","pw","vw","pw"]]"""


bot.run(TOKEN)
