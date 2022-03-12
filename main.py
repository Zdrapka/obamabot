#!/usr/bin/env python3
import asyncio

import asyncpg
import discord
from discord.ext import commands

from cogs.utils.default import Obamabot
from cogs.utils import config as cfg


async def run():
    intents = discord.Intents.default()
    intents.message_content = True

    db = asyncpg.create_pool(**cfg.POSTGRES_CREDS)

    prefix = commands.when_mentioned_or(cfg.PREFIX)

    bot = Obamabot(
        command_prefix=prefix,
        db=db,
        intents=intents,
    )

    try:
        await bot.start(cfg.TOKEN)
    except KeyboardInterrupt:
        await db.close()
        await bot.logout()


if __name__ == "__main__":
    asyncio.run(run())
