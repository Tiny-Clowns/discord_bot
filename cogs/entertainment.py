from discord.ext import commands
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


async def setup(bot):
    await bot.add_cog(Entertainment(bot))