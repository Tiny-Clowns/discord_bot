import discord
from discord.ext import commands

# The discord command prefix is !
COMMAND_PREFIX = "!"


def read_token():
    try:
        file=open("token.txt", "r")
        return file.readline()

    except Exception as ex:
        print(ex)







bot = commands.Bot(intents=discord.Intents.all(), command_prefix=COMMAND_PREFIX)

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong!\nLatency: {bot.latency}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required arguments.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Bad argument provided.")
    else:
        await ctx.send("An error occurred.")




bot.run(read_token())

