import os

import asyncpg
import discord
from discord.ext import commands

from cogs.utils.config import DEBUG_GUILD


class Obamabot(commands.Bot):
    """Custom bot subclass"""

    def __init__(
        self,
        command_prefix,
        help_command=None,
        description=None,
        **options,
    ):
        super().__init__(
            command_prefix,
            help_command,
            description,
            **options,
        )

        self.db: asyncpg.Pool = options.pop("db")
        assert self.db is not None, "db is None"

    async def startup(self):
        await self.wait_until_ready()
        await self.tree.sync(guild=discord.Object(id=DEBUG_GUILD))
        print("Successfully synced applications commands")

        print(
            f"Logged in as {self.user} (ID: {self.user.id})\n"
            f"Guilds: {len(self.guilds)}"
        )

    async def setup_hook(self):
        for f in os.listdir("./cogs"):
            if f.endswith(".py"):
                await self.load_extension(f"cogs.{f[:-3]}")
                print(f"Loaded {f}")

        self.loop.create_task(self.startup())
