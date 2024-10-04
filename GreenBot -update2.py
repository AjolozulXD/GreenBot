import discord
from discord.ext import commands, tasks
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

# Lista de artículos contaminantes
articulos = ("Los artículos de uso diario que más contaminan suelen ser aquellos que generan residuos plásticos, electrónicos y productos desechables. Algunos de los más comunes son:\n"
             "1. Botellas de plástico: Las botellas de agua o refrescos de plástico son uno de los residuos más abundantes y tardan cientos de años en degradarse, contaminando océanos y suelos.\n"
             "2. Envases y empaques de comida: Los envases de comida rápida, envoltorios de snacks y plásticos de un solo uso (como cubiertos, pajitas y vasos) generan grandes cantidades de residuos.\n"
             "3. Electrónica de un solo uso o desechable: Los cargadores de dispositivos, pilas y algunos gadgets baratos se desechan rápidamente, y su fabricación y descomposición liberan materiales tóxicos.\n"
             "4. Productos de higiene personal desechables: Pañuelos, toallas húmedas, hisopos, y productos similares de uso cotidiano que no son biodegradables también representan un riesgo ambiental significativo."
             )

@bot.command()
async def materialesConta(ctx):
    await ctx.send(f"{articulos}\n\nEstos son algunos de los artículos de uso diario que suelen contaminar más.")

# Información general sobre la contaminación
@bot.command()
async def info(ctx):
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

# Ideas de reciclaje automáticas cada cierto tiempo
@tasks.loop(hours=10)
async def enviar_idea_reciclaje():
    canal = bot.get_channel("id del canal")  # Hay que poner la id del canal de discord sin las comillas
    idea = random.choice(ideas)
    await canal.send(f"♻️ ¡Aquí tienes una nueva idea de reciclaje! 🌿: {idea}")

# Comienza la tarea automática de envío de ideas de reciclaje
@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")
    enviar_idea_reciclaje.start()

@bot.command()
async def ayudar(ctx):
    await ctx.send("Para ayudar a cuidar el planeta puedes optar por seguir las reglas de las 3 R: Reducir, Reutilizar y Reciclar. También puedes unirte a ONGs centradas en el medio ambiente. Recuerda que cada acción es de gran aporte para cuidar nuestro planeta, tu hogar y el de muchos más")

# Ejemplo de materiales ecológicos
materiales_eco = [
    "Bambú: Un recurso renovable y biodegradable.",
    "Algodón orgánico: Cultivado sin pesticidas y productos químicos dañinos.",
    "Vidrio reciclado: Material duradero y reutilizable.",
    "Corcho: Extraído de árboles sin dañarlos, es resistente y sostenible.",
    "Madera certificada: Procedente de bosques gestionados de manera sostenible."
]

@bot.command()
async def materialesEco(ctx):
    material = random.choice(materiales_eco)
    await ctx.send(f"🌿 Material ecológico: {material}")

bot.run("Tu token aquí, hermos@")
