from inspect import cleandoc

import discord
from discord.commands import slash_command, Option

from cogs.utils import ObamaBot, CONFIG


class Information(discord.Cog):
    """Information stuff"""

    def __init__(self, bot: ObamaBot):
        self.bot = bot

    @slash_command()
    async def ping(self, ctx: discord.ApplicationContext):
        """Get the bot's ping"""

        await ctx.respond(f"Pong! {round(self.bot.latency * 1000)}ms")

    @slash_command()
    async def about(self, ctx: discord.ApplicationContext):
        """About the bot!"""

        me = f"<@{self.bot.owner_id}>"

        desc = (
            f"A leveling bot made by a nerd ({me}) who literally procrastinates"
            "just to get this bot to work. You're welcome. Always remember: there is no"
            "sacrifice too great."
            "\n"
            "The main focus of this bot is to be a FREE, CUSTOMIZABLE, and"
            "FULLY-FEATURED leveling bot for Discord. It's a work in progress, so"
            "expect bugs and glitches. If you find any, please report them to"
            f"{me} and I will *try* to fix them. I don't guarantee anything, though."
        )

        e = discord.Embed(
            title=f"About {self.bot.user}",
            description=desc,
        )
        e.set_thumbnail(url=self.bot.user.display_avatar.url)

        await ctx.respond(embed=e)


def setup(bot: ObamaBot):
    bot.add_cog(Information(bot))
