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
            await ctx.send(f"Sorry, {ctx.author.mention} Command not found.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry, {ctx.author.mention} you provided missing required arguments.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"Sorry, {ctx.author.mention} you provided a bad argument.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Sorry, {ctx.author.mention} you do not have the permissions to do that.")
        elif isinstance(error, commands.MissingRole):
            await ctx.send(f"Sorry, {ctx.author.mention} you do not have the role to do that.")
        else:
            await ctx.send("An error occurred.\n" + str(error))

async def setup(bot):
    await bot.add_cog(Common(bot))

