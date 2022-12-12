# cogs/listing.py

"""
Message Manager - A bot for discord
Copyright (C) 2020-2021 AnotherCat

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import logging

from typing import TYPE_CHECKING

from discord.ext import commands, tasks

from main import Bot
from src import Context, list_wrappers

if TYPE_CHECKING:
    Cog = commands.Cog[Context]
else:
    Cog = commands.Cog


logger = logging.getLogger(__name__)


class ListingCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        self.stats_post_loop.start()
        self.de_list = list_wrappers.Del(token=self.bot.del_token, bot=self.bot)
        self.dbl = list_wrappers.Dbl(token=self.bot.dbl_token, bot=self.bot)
        self.dboats = list_wrappers.DBoats(token=self.bot.dboats_token, bot=self.bot)
        self.dbgg = list_wrappers.Dbgg(token=self.bot.dbgg_token, bot=self.bot)
        self.topgg = list_wrappers.TopGG(token=self.bot.topgg_token, bot=self.bot)

    def cog_unload(self) -> None:
        self.stats_post_loop.cancel()

    @tasks.loop(minutes=30)
    async def stats_post_loop(self) -> None:
        await self.bot.wait_until_ready()
        await self.de_list.post_guild_stats()
        await self.dbl.post_guild_stats()
        await self.dboats.post_guild_stats()
        await self.dbgg.post_guild_stats()
        await self.topgg.post_guild_stats()


def setup(bot: Bot) -> None:
    bot.add_cog(ListingCog(bot))
    logger.info("Listing cog!")
