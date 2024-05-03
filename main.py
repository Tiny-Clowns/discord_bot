import discord
from discord.ext import commands
import random

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


@bot.command()
async def random_teams(ctx, team_quantity: int, *names):
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


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required arguments.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Bad argument provided.")
    else:
        await ctx.send("An error occurred.\n" + str(error))




bot.run(read_token())

