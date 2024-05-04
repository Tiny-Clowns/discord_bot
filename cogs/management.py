from discord.ext import commands
from discord import Embed, Color

class Management(commands.Cog):   
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, quantity: int):
        if ((0<quantity) and (quantity<101)):
            messages = await ctx.channel.purge(limit=quantity+1)

            embed=Embed(title="✅Messages successfully cleared!", color=Color.blue())
            embed.add_field(name="Requested by", value=f"{ctx.author.mention}", inline=False)
            embed.add_field(name="Requested", value=f"{quantity}", inline=False)
            embed.add_field(name="Cleared", value=f"{len(messages)-1}", inline=False)
            embed.set_footer(text="This message will be deleted automatically in 5 seconds.")

            await ctx.send(embed=embed, delete_after=5)

        else:
            embed=Embed(title="❌Purge unsuccessful", color=Color.blue())
            embed.add_field(name="Hint", value=f"Please ensure the purge quantity is an integer between 1 and 100.", inline=False)
            embed.add_field(name="Requested by", value=f"{ctx.author.mention}", inline=False)
            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Management(bot))