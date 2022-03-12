import os
import asyncpg
import discord
from discord.ext import commands


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

        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                self.load_extension(f"cogs.{file[:-3]}")

    async def on_ready(self):
        print(
            f"Logged in as {self.user} (ID: {self.user.id})\n"
            f"Guilds: {len(self.guilds)}"
        )
