import time

import discord
from discord import app_commands
from discord.ext import commands

from cogs.utils.default import Obamabot


class Info(commands.Cog):
    """General information commands"""

    def __init__(self, bot: Obamabot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Pong!"""

        t1 = time.perf_counter()
        msg = await ctx.send("Testing ping...")
        t2 = time.perf_counter()

        lag = round((t2 - t1) * 1000)
        latency = round(self.bot.latency * 1000)
        await msg.edit(content=f"Pong! `{lag}`ms\n(API: `{latency}`ms)")

    @commands.command()
    async def about(self, ctx: commands.Context):
        """Get to know about the bot!"""

        await ctx.send("Work in progress")


async def setup(bot):
    await bot.add_cog(Info(bot))
