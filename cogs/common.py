from discord.ext import commands

class Common(commands.Cog):   
    def __init__(self, bot):
        self.bot=bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong!\nLatency: {self.bot.latency}")


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required arguments.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Bad argument provided.")
        else:
            await ctx.send("An error occurred.\n" + str(error))

async def setup(bot):
    await bot.add_cog(Common(bot))

