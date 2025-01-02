import discord
from discord.ext import commands
from dotenv import load_dotenv 
import os

load_dotenv()

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/',intents=intents)
bot_token = os.getenv('BOT_TOKEN')

@client.tree.command(name='ping', description='Returns the latency of the bot')
async def ping(interaction:discord.Interaction):
    ctx = await commands.Context.from_interaction(interaction)
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

client.run(bot_token)
