import discord
from discord.ext import commands
import os

# Create an instance of the bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

async def load_cogs():
    # List to store loaded cog names
    loaded_cogs = []

    # Iterate over files in the modules directory
    modules_dir = './modules'
    for filename in os.listdir(modules_dir):
        if filename.endswith('.py'):
            cog_name = filename[:-3]  # Remove the .py extension
            try:
                await bot.load_extension(f'modules.{cog_name}')
                loaded_cogs.append(cog_name)
            except Exception as e:
                print(f'Failed to load cog {cog_name}: {e}')

    return loaded_cogs

@bot.event
async def on_ready():
    loaded_cogs = await load_cogs()
    print("Thanks For Using The z3r Project!")
    print("jqm1e.xyz/z3r")
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Loaded cogs:')
    for cog in loaded_cogs:
        print(f'- {cog}')

# Start the bot with your token
bot.run('MTI3NjEwMzM2NDgxMTE2MTYzMA.G54h11.5IQU4H_fqwW4csA0X1ZTkDLNs0YhSjiNa21dZk')
