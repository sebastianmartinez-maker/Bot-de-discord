from dotenv import load_dotenv
import os, random
import discord
import botlogic as logic
from discord.ext import commands
import requests

load_dotenv()
token = os.getenv("dt")

# Configurar permisos del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='29', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command(name="psw")
async def passw(ctx, lenght=25):
    x = logic.gen_pass(lenght)
    await ctx.send(f"🔒 Contraseña generada: `{x}`")

"""@bot.command(name="yt")
async def youtube(ctx, *, url):
    if not ctx.voice_client:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("❌ Debes estar conectado a un canal de voz.")
            return

    async with ctx.typing():
        player = await logic.YTDLSource.from_url(url, loop=bot.loop)
        ctx.voice_client.play(player, after=lambda e: print(f"Error: {e}") if e else None)

    await ctx.send(f"🎶 Reproduciendo ahora: **{player.title}**")"""

@bot.command(name="meme")
async def mm(ctx):
    x = logic.meme()
    await ctx.send(file=x)

@bot.command(name="memes")
async def mms(ctx):
    x = logic.memes()
    await ctx.send(file=x)

@bot.command()
async def animales(ctx):
    animales = ['img/meme1.jpeg', 'img/meme2.jpeg', "img/meme3.jpeg"  ]
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable
    # A continuación, podemos enviar este archivo como parámetro.
    random_animal = random.choice(animales)
    with open(random_animal, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command(name="patos")
async def patos(ctx):
    x = logic.get_duck_image_url()
    await ctx.send(x)

@bot.command(name="anime")
async def anime(ctx, *, q):
    anime_data = logic.anime_url(q)
    if anime_data:
        for ani in anime_data:
            try:
                title = ani["attributes"]["canonicalTitle"]
                img_url = ani["attributes"]["posterImage"]["small"]
                await ctx.send(f"**{title}**\n{img_url}")
            except KeyError:
                continue
    else:
        await ctx.send("❌ No se encontraron datos de este anime.")




@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")

@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"""
    Hola, soy {bot.user}!
    """)# esta linea saluda
    await ctx.send("¿Quieres hablar de Dragon Ball Super?")
    # Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content == 'si':
            await ctx.send("""Dragon Ball Super es un mmanga creado por Akira Toriyama donde continuan las aventuras de Goku y sus amigos""")   
        else:
            await ctx.send("Está bien, si alguna vez necesitas saber algo más de Dragon Ball Super, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
 
    await ctx.send("¿Quieres conocer Las sagas de Dragon Ball Super?, responde 'sí' o 'no'.")
    def check1(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response1 = await bot.wait_for('message', check=check1)
    if response1:
        if response1.content == "si":
            await ctx.send("1. La saga de la resurrección de Freezer") 
            await ctx.send("2. La saga de Goku black") 
            await ctx.send("3. La saga del torneo del poder")
            await ctx.send("4. La saga de Moro") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas conocer las sagas De DBS, me avisas.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Deseas ver una imagen sobre un ejemplo de Dragon Ball super?")
    def check2(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response2 = await bot.wait_for('message', check=check2)
    if response2:
        if response2.content == "si":
            with open('img/meme13.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
                picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=picture)
        else:
            await ctx.send("Esta bien!")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")


bot.run(token)
