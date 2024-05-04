from discord.ext import commands

class Management(commands.Cog):   
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, quantity: int):
        if ((0<quantity) and (quantity<101)):
            messages = await ctx.channel.purge(limit=quantity+1)
            await ctx.send(f"Cleared {len(messages)-1} messages. (This message will be deleted automatically in 3 seconds.)", delete_after=3)

        else:
            await ctx.send(f"Sorry, {ctx.author.mention} minimum purge quantity is 1, maximum is 100. You requested {quantity}.")


async def setup(bot):
    await bot.add_cog(Management(bot))