import discord
from discord.ext import commands

from cogs.utils.default import Obamabot


class Developer(commands.Cog):
    """Developer commands"""

    def __init__(self, bot: Obamabot):
        self.bot = bot

    @commands.command()
    async def reload(self, ctx: commands.Context, extension: str):
        """Reload an extension"""

        try:
            self.bot.reload_extension(f"cogs.{extension}")
            await ctx.send(f"Reloaded `{extension}`")
        except Exception as e:
            await ctx.send(f"Error! ```py\n{e}\n```")

    @commands.command()
    async def load(self, ctx: commands.Context, extension: str):
        """Load an extension"""

        try:
            self.bot.load_extension(f"cogs.{extension}")
            await ctx.send(f"Loaded `{extension}`")
        except Exception as e:
            await ctx.send(f"Error! ```py\n{e}\n```")

    @commands.command()
    async def unload(self, ctx: commands.Context, extension: str):
        """Unload an extension"""

        try:
            self.bot.unload_extension(f"cogs.{extension}")
            await ctx.send(f"Unloaded `{extension}`")
        except Exception as e:
            await ctx.send(f"Error! ```py\n{e}\n```")


def setup(bot):
    bot.add_cog(Developer(bot))
