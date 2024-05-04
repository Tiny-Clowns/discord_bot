import discord
from discord.ext import commands
from utility import read_token
import os
import asyncio
import datetime


# The discord command prefix is !
COMMAND_PREFIX = "!"
    

async def main():
    bot = commands.Bot(intents=discord.Intents.all(), command_prefix=COMMAND_PREFIX)

    # Log all cogs under cogs folder
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded {filename}")


    bot.start_time=datetime.datetime.now()

    await bot.start(read_token())


if __name__ == "__main__":
    asyncio.run(main())