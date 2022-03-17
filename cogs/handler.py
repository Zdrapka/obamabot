import traceback
import discord
from discord.ext import commands

from cogs.utils.default import Obamabot


class GlobalHandler(commands.Cog):
    """Global command error handler"""

    def __init__(self, bot: Obamabot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(
        self, ctx: commands.Context, error: commands.CommandError
    ):
        """Handle errors"""

        match error:
            case commands.CommandNotFound() | commands.NotOwner():
                return

            case commands.MissingRequiredArgument():
                return await ctx.send(
                    f"`{error.param.name}` is required. Fill in the blanks!\n"
                    f"See `{ctx.prefix}help {ctx.command}` for more info."
                )

            case commands.MissingPermissions():
                return await ctx.send("You do not have the required permissions!")

                # TODO add a button that then sends a message that
                # lets the user know what permissions are missing

            case _:
                raise error from error


async def setup(bot):
    await bot.add_cog(GlobalHandler(bot))
