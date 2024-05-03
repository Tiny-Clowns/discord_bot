from discord.ext import commands
from discord.utils import get
import random

class Entertainment(commands.Cog):   
    def __init__(self, bot):
        self.bot=bot
    
    @commands.command()
    async def random_teams(self, ctx, team_quantity: int, *names):
        if (team_quantity < 2):
            await ctx.send("Please provide a valid team quantity. (Min 2)")
            return
        
        team_player_quantity = len(names)

        if (team_player_quantity < team_quantity):
            await ctx.send(f"Not enough players to form teams.\nPlayer quantity provided: {team_player_quantity}\nTeam quantity provided: {team_quantity}\n\nYou need to provide {team_quantity-team_player_quantity} more player(s) to proceed.")
            return

        names = list(names)
        random.shuffle(names)
        teams = [names[i::team_quantity] for i in range(team_quantity)]

        for i, team in enumerate(teams, 1):
            await ctx.send(f"Team {i}: {', '.join(team)}")

    @commands.command()
    @commands.has_permissions(move_members=True)
    async def split(self, ctx):
        current_voice_channel = ctx.author.voice.channel

        new_channel_1 = get(ctx.guild.voice_channels, name="Team 1")
        new_channel_2 = get(ctx.guild.voice_channels, name="Team 2")

        if not new_channel_1:
            new_channel_1 = await ctx.guild.create_voice_channel(name="Team 1")

        if not new_channel_2:
            new_channel_2 = await ctx.guild.create_voice_channel(name="Team 2")

        # Get a list of members in the source channel
        members = [member.id for member in current_voice_channel.members]
        
        random.shuffle(members)

        for i, member_id in enumerate(members):
            member = ctx.guild.get_member(member_id)
            if member:
                if i % 2 == 0:
                    await member.move_to(new_channel_1)
                else:
                    await member.move_to(new_channel_2)
        
        await ctx.send(f"Members from {current_voice_channel.name} have been split between {new_channel_1.name} and {new_channel_2.name}.")


async def setup(bot):
    await bot.add_cog(Entertainment(bot))