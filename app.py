from dotenv import load_dotenv
import os, discord, botlogic as logic
from discord.ext import commands
load_dotenv()

token = os.getenv("dt")
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios

bot = commands.Bot(command_prefix='29', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name = "psw")
async def passw(ctx, lenght = 25):
    x = logic.gen_pass(lenght)
    await ctx.send(f"🔒contraseña generada:{x}")

@bot.command(name = "yt")
async def youtube(ctx, *, url):
    if not ctx.voice_client:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.sent("❌Debes estar conectado a un canal de voz para estar conectado")
            return
        
    async with ctx.typing():
        player = await logic.YTDLSource, from_url(url, Loop = bot.loop)
        ctx.voice_client.play(player, ofter = lamda e: print(f"error{e}")if e else None)

    await ctx.send(f"🎶 Reproduciendo ahora: **{player.title}**")




bot.run(token)