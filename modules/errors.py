# errors.py
import discord
from discord.ext import commands
import traceback


class ErrorReporting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def log_error(self, error_message):
        """Logs the error to console."""



        # Print the error message to the console
        print(f"Error: {error_message}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handles command errors."""
        # Create an error message
        error_message = f"Error in command '{ctx.command}': {traceback.format_exc()}"

        # Log the error
        await self.log_error(error_message)

        # Send a user-friendly error message
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found. Use `!help` to see the list of commands.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required argument. Please check the command usage.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument. Please check the command usage.")
        else:
            await ctx.send("An error occurred while executing the command.")


async def setup(bot):
    await bot.add_cog(ErrorReporting(bot))
