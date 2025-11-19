import discord
from discord.ext import commands

# Remplace par ton token
TOKEN = "MTQzODE5ODc0MTQ5NTU3ODY4NA.GDN8aq.A3Tl8m1bcVld2efrEctG6SGIjyvTXenwJAxGac"

# Définir les intentions (pour que ton bot voie les messages)
intents = discord.Intents.default()
intents.message_content = True

# Préfixe pour les commandes (ex: !ping)
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

plateau_mat = [
    ["pb","vw","pb","vw","pb","vw","pb","vw","pb","vw"],\
    ["vw","pb","vw","pb","vw","pb","vw","pb","vw","pb"],\
    ["pb","vw","pb","vw","pb","vw","pb","vw","pb","vw"],\
    ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
    ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
    ["vw","vb","vw","vb","vw","vb","vw","vb","vw","vb"],\
    ["vb","vw","vb","vw","vb","vw","vb","vw","vb","vw"],\
    ["vw","pw","vw","pw","vw","pw","vw","pw","vw","pw"],\
    ["pw","vw","pw","vw","pw","vw","pw","vw","pw","vw"],\
    ["vw","pw","vw","pw","vw","pw","vw","pw","vw","pw"]]
PION_WHITE = "<:pion_blanc:1440245376673251348>"
PION_BLACK = "<:pion_noire:1440245418557706290>"
DAME_WHITE="<:dame_blanche:1440245260650287224>"
DAME_BLACK="<:dame_noire:1440245307328958534>"
VIDE_BROWN="<:vide_marron:1440255154837520415>"
VIDE_WHITE=":white_large_square:"
emojis={"pw":PION_WHITE,"pb":PION_BLACK,"dw":DAME_WHITE,"db":DAME_BLACK,"vb":VIDE_BROWN,"vw":VIDE_WHITE}

@bot.command()
async def ping(ctx):
    await ctx.send("Pong ! 🏓")
@bot.command()
async def hi(ctx):
    await ctx.send("Hello")
@bot.command()
async def plateau(ctx):
    for i in plateau_mat:
        msg = "".join(emojis[j] for j in i)
        await ctx.send(msg)
bot.run(TOKEN)
