# modules/logging.py
from discord.ext import commands
from discord import Embed, Colour
from datetime import datetime


class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


        self.log_channels = {
            'role': 1292390835022860359,
            'join': 1292390823291260938,
            'leave': 1292390823291260938,
            'message_delete': 1292390856317341716,
            'message_edit': 1292390856317341716,
            'reaction_add': 1292390871219572810,
            'reaction_remove': 1292390882838057064,
            'role_create': 1292390835022860359,
            'role_delete': 1292390835022860359,
            'channel_create': 1292391760022212618,
            'channel_delete': 1292391760022212618,

        }

    async def log(self, action: str, title: str, description: str, user=None):
        """Send a log message to the appropriate log channel."""
        channel_id = self.log_channels.get(action)
        if channel_id:
            channel = self.bot.get_channel(channel_id)
            if channel:
                embed = Embed(title=title, description=description, color=Colour.blue())
                embed.set_footer(
                    text=f"Action logged by {user} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" if user else f"Action logged at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Log when a member joins the server."""
        await self.log('join', 'Member Joined', f"{member.mention} has joined the server.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """Log when a member leaves the server."""
        await self.log('leave', 'Member Left', f"{member.mention} has left the server.")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """Log role changes for a member."""
        added_roles = [role for role in after.roles if role not in before.roles]
        removed_roles = [role for role in before.roles if role not in after.roles]

        if added_roles:
            await self.log('role', 'Role Added',
                           f"{after.mention} has been given the role(s): {', '.join(role.name for role in added_roles)}.",
                           after)

        if removed_roles:
            await self.log('role', 'Role Removed',
                           f"{after.mention} has lost the role(s): {', '.join(role.name for role in removed_roles)}.",
                           after)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """Log when a message is deleted."""
        if message.author.bot:
            return
        await self.log('message_delete', 'Message Deleted',
                       f"Message from {message.author.mention}: {message.content} (Channel: {message.channel.mention})",
                       message.author)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        """Log when a message is edited."""
        if before.author.bot:
            return
        await self.log('message_edit', 'Message Edited',
                       f"Message from {before.author.mention} edited in {before.channel.mention}.\n**Before:** {before.content}\n**After:** {after.content}",
                       before.author)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        """Log when a reaction is added to a message."""
        if user.bot:
            return
        await self.log('reaction_add', 'Reaction Added',
                       f"{user.mention} reacted with {reaction.emoji} to a message in {reaction.message.channel.mention}.",
                       user)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        """Log when a reaction is removed from a message."""
        if user.bot:
            return
        await self.log('reaction_remove', 'Reaction Removed',
                       f"{user.mention} removed their {reaction.emoji} reaction from a message in {reaction.message.channel.mention}.",
                       user)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        """Log when a role is created."""
        await self.log('role_create', 'Role Created', f"The role '{role.name}' has been created.")

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        """Log when a role is deleted."""
        await self.log('role_delete', 'Role Deleted', f"The role '{role.name}' has been deleted.")

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        """Log when a channel is created."""
        await self.log('channel_create', 'Channel Created', f"The channel '{channel.name}' has been created.")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        """Log when a channel is deleted."""
        await self.log('channel_delete', 'Channel Deleted', f"The channel '{channel.name}' has been deleted.")


async def setup(bot):
    await bot.add_cog(Logger(bot))
