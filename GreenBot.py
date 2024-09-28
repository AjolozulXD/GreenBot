import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="G", intents=intents)

#lista de materiales que suelen contaminar más
articulos = ("Los artículos de uso diario que más contaminan suelen ser aquellos que generan residuos plásticos, electrónicos y productos desechables. Algunos de los más comunes son:\n"
             "1. Botellas de plástico: Las botellas de agua o refrescos de plástico son uno de los residuos más abundantes y tardan cientos de años en degradarse, contaminando océanos y suelos.\n"
             "2. Envases y empaques de comida: Los envases de comida rápida, envoltorios de snacks y plásticos de un solo uso (como cubiertos, pajitas y vasos) generan grandes cantidades de residuos.\n"
             "3. Electrónica de un solo uso o desechable: Los cargadores de dispositivos, pilas y algunos gadgets baratos se desechan rápidamente, y su fabricación y descomposición liberan materiales tóxicos.\n"
             "4. Productos de higiene personal desechables: Pañuelos, toallas húmedas, hisopos, y productos similares de uso cotidiano que no son biodegradables también representan un riesgo ambiental significativo."
             )

@bot.command()
async def materialesContaminantes(ctx):
    await ctx.send(f"{articulos}\n\nEstos son algunos de los artículos de uso diario que suelen contaminar más.")


@bot.command()
async def contaminacionINFO(ctx):
    await ctx.send("La contaminación es un problema que cada día es más preocupante. Según la OMS, el 99% de la población mundial respira aire insalubre, esto debido a los gases que sueltan los carros, descomposición de materiales, etc...")

# Lista de ideas de reciclaje
ideas = [
    "Usa botellas de plástico vacías como macetas para plantas pequeñas.",
    "Convierte latas viejas en portalápices decorados.",
    "Utiliza cajas de cartón para crear organizadores de escritorio.",
    "Haz papel reciclado con periódicos viejos.",
    "Reutiliza frascos de vidrio como envases para alimentos.",
    "Convierte ropa vieja en trapos de limpieza.",
    "Usa tubos de papel higiénico para organizar cables.",
    "Haz una compostera casera con desechos orgánicos."
]

@bot.command()
async def reciclar(ctx):
    idea = random.choice(ideas)
    await ctx.send(f"🌱 Idea de reciclaje: {idea}")

@bot.command()
async def ayudar(ctx):
    await ctx.send("Para ayudar a cuidar el planeta puedes optar por seguir las reglas de las 3 R: Reducir, Reutilizar y Reciclar. También puedes unirte a ONGs centradas en el medio ambiente. Recuerda que cada acción es de gran aporte para cuidar nuestro planeta, tu hogar y el de muchos más")


bot.run("token")