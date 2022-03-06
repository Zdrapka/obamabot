import asyncio

# import discord

from cogs.utils import ObamaBot, CONFIG

TOKEN = (
    CONFIG["token"]["production"]
    if CONFIG["is_production"]
    else CONFIG["token"]["development"]
)


def main():
    bot = ObamaBot()
    bot.run(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
