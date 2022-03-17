import discord
from discord.ext import commands

from cogs.utils.default import Obamabot


class Developer(commands.Cog):
    """Developer commands"""

    def __init__(self, bot: Obamabot):
        self.bot = bot

    async def cog_command_error(
        self, ctx: commands.Context, error: commands.CommandError
    ):
        """Cog-specific error handlers"""

        match error:
            case commands.ExtensionAlreadyLoaded():
                await ctx.send(f"`{error.name}` is already loaded!")

            case _:
                await ctx.send(f"Error! \n```py\n{error}\n```")

    @commands.command()
    async def reload(self, ctx: commands.Context, extension: str):
        """Reload an extension"""

        await self.bot.reload_extension(f"cogs.{extension}")
        await ctx.send(f"Reloaded `{extension}`")

    @commands.command()
    async def load(self, ctx: commands.Context, extension: str):
        """Load an extension"""

        await self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded `{extension}`")

    @commands.command()
    async def unload(self, ctx: commands.Context, extension: str):
        """Unload an extension"""

        await self.bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded `{extension}`")


async def setup(bot):
    await bot.add_cog(Developer(bot))
