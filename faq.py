import datetime
from logging import getLogger

import aiohttp
from discord import Client, Object, app_commands
from discord.ext import commands

from config import Config

log = getLogger(__name__)

config = Config().load()
ModMail_Support = Object(id=Config().MAIN_GUILD)


class FAQ_Client(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_time = datetime.datetime.utcnow()
        self.tree = app_commands.CommandTree(self)

    @property
    def uptime(self):
        return datetime.datetime.utcnow() - self.start_time

    @property
    def version(self):
        return Config().VERSION

    @property
    def config(self):
        return Config()

    async def setup_hook(self) -> None:
        print(
            "------",
            f"Logged in as: {self.user}",
            f"ID: {self.user.id}",
            f"Version: {self.version}",
            f"Started at: {datetime.datetime.utcnow()}",
            "------",
            sep="\n",
        )
        self.tree.copy_global_to(guild=ModMail_Support)
        await self.tree.sync(guild=ModMail_Support)

    async def main(self):
        async with aiohttp.ClientSession() as session:
            async with self:
                self.session = session
                try:
                    await self.start(self.config.TOKEN)
                    print("Started successfully withtoken attribute")
                except Exception as e:
                    print(f"Failed to start: {e}")
                    await self.start(Config().TOKEN)
