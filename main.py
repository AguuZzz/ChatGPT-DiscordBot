import discord
import openai
import keep_alive # A 24/7 module
from discord.ext import commands

description = '''Discord bot'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# NEED A API KEY
openai.api_key = TOKEN
  
bot = commands.Bot(command_prefix='!', description=description, intents=intents) # Replace "!" for you fav prefix



@bot.event
async def on_ready():
    print("Bot online")


#Chat gpt
@bot.command()
async def chatgpt(ctx, *, text):
    await ctx.send(f'Cargando resultados de: "{text}"')
    pedido = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"{text}",
    max_tokens=2000,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    resultado = pedido["choices"][0]["text"]
    await ctx.send(resultado)


keep_alive.keep_alive()
bot.run(TOKEN)
