from discord.ext import commands

class Management(commands.Cog):   
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def clear(self, ctx, quantity: int):

        if ((0<quantity) and (quantity<101)):
            messages = await ctx.channel.purge(limit=quantity+1)

            await ctx.send(f"Cleared {len(messages)-1} messages", delete_after=3)

        else:
            await ctx.send(f"Sorry, minimum purge quantity is 1, maximum is 100. You requested {quantity}.")


async def setup(bot):
    await bot.add_cog(Management(bot))