
import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
   await client.change_presence(activity=discord.Streaming(name="LumberCraft", url="https://www.twitch.tv/yamil010"))
   print('LumberCraft is Ready')

client.run(os.getenv('TOKEN'))
