import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!lc')

@client.event
async def on_ready():
   await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="LumberCraft"))
   print('LumberCraft is Ready')

client.run(os.getenv('TOKEN'))
