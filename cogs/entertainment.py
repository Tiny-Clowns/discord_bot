from discord.ext import commands
from discord.utils import get
import random
from discord import Embed, Color


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

        embed=Embed(title="Random teams result", color=Color.blue())
        embed.add_field(name="Requested by", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name="Team quantity", value=team_quantity, inline=False)
        

        for i, team in enumerate(teams, 1):
            embed.add_field(name=f"Team {i}", value=team, inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def split(self, ctx):
        if (ctx.author.voice==None):
            await ctx.send(f"Sorry, {ctx.author.mention} you have not joined any voice channels in this server yet.")
            return
        
        current_voice_channel = ctx.author.voice.channel

        new_channel_1_name = "Team 1"
        new_channel_2_name = "Team 2"

        new_channel_1 = get(ctx.guild.voice_channels, name=new_channel_1_name)
        new_channel_2 = get(ctx.guild.voice_channels, name=new_channel_2_name)
        category = get(ctx.guild.categories, name="Split team")

        if not category:
            category = await ctx.guild.create_category("Split team")

        if not new_channel_1:
            new_channel_1 = await ctx.guild.create_voice_channel(name=new_channel_1_name, category=category)

        if not new_channel_2:
            new_channel_2 = await ctx.guild.create_voice_channel(name=new_channel_2_name, category=category)

        # Get a list of members in the source channel
        members = [member.id for member in current_voice_channel.members]
        
        random.shuffle(members)
        allocation = {new_channel_1_name: [], new_channel_2_name: []}

        for i, member_id in enumerate(members):
            member = ctx.guild.get_member(member_id)
            if member:
                if i % 2 == 0:
                    await member.move_to(new_channel_1)
                    allocation[new_channel_1_name].append(member.name)
                else:
                    await member.move_to(new_channel_2)
                    allocation[new_channel_2_name].append(member.name)
        
        embed=Embed(title="Split result", color=Color.blue())
        embed.add_field(name="Requested by", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name="Moved from", value=f"{current_voice_channel}", inline=False)
        embed.add_field(name=new_channel_1_name, value=f"{allocation[new_channel_1_name]}", inline=False)
        embed.add_field(name=new_channel_2_name, value=f"{allocation[new_channel_2_name]}", inline=False)

        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(Entertainment(bot))