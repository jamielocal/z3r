# modules/one.py
from discord.ext import commands

class TestingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("github.com/jamielocal/z3r | Loaded Modules. Thanks For Using This | Check Out Plugins and Translations At jqm1e.xyz/z3r")

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("Testing Cog Included In z3r | https://github.com/jamielocal/z3r")

async def setup(bot):
    await bot.add_cog(TestingCog(bot))
