from discord.ext import commands
from discord import Embed, Color

class Common(commands.Cog):   
    def __init__(self, bot):
        self.bot=bot
    
    @commands.command()
    async def ping(self, ctx):
        embed=Embed(title="Pong!", color=Color.blue())
        embed.add_field(name="Latency", value=f"{round(self.bot.latency*1000, 2)} ms", inline=False)

        await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Sorry, {ctx.author.mention} Command not found.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry, {ctx.author.mention} you provided missing required arguments.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"Sorry, {ctx.author.mention} you provided a bad argument.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Sorry, {ctx.author.mention} you do not have the permission to do that.")
        elif isinstance(error, commands.MissingRole):
            await ctx.send(f"Sorry, {ctx.author.mention} you do not have the role to do that.")
        else:
            await ctx.send("An error occurred.\n" + str(error))

async def setup(bot):
    await bot.add_cog(Common(bot))

