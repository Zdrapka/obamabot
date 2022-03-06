from datetime import datetime
from inspect import cleandoc
import os
import discord

# from discord.ext import commands

from cogs.utils.config import CONFIG

# pylint: disable=abstract-method, useless-super-delegation


class ObamaBot(discord.Bot):
    """Main bot subclass"""

    def __init__(self, **options):
        intents = discord.Intents.all()

        super().__init__(
            intents=intents,
            debug_guilds=CONFIG["debug_guilds"],
            owner_id=CONFIG["owner_id"],
            **options,
        )

        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                self.load_extension(f"cogs.{file[:-3]}")

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")


class DefaultEmbed(discord.Embed):
    """Overridden `Embed` class to provide more default values.

    Parameter Aliases:

    color: colour
    description: desc
    timestamp: ts
    """

    def __init__(self, **kwargs):
        default_color = int(CONFIG["default_embed_color"].replace("#", ""), base=16)

        super().__init__(
            color=kwargs.get("color", kwargs.get("colour", default_color)),
            title=kwargs.get("title", None),
            type=kwargs.get("type", None),
            url=kwargs.get("url", None),
            description=cleandoc(kwargs.get("description", kwargs.get("desc", None))),
            timestamp=kwargs.get("timestamp", kwargs.get("ts", datetime.now())),
        )

    def add_field(self, *, name: str, value: str, inline: bool = True):
        return super().add_field(name=name, value=cleandoc(value), inline=inline)
