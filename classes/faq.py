from datetime import datetime
from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING, Formatter, getLogger
from logging.handlers import RotatingFileHandler

from aiohttp import ClientSession
from discord import Activity, ActivityType, Client, Intents, Object, app_commands
from mappings import log_levels

from classes.config import Config
from classes.views import PersistentView

intents = Intents.default()
intents.message_content = True
intents.members = True
intents.emojis = True


class FAQ_Client(Client):
    def __init__(self, *args, web_client: ClientSession, **kwargs):
        super().__init__(**kwargs)
        self.start_time = datetime.utcnow()
        self.tree = app_commands.CommandTree(self)
        self.config = Config().load()
        self.testing_guild = Object(self.config.TESTING_GUILD)
        self.version = self.config.VERSION
        self.log_level = log_levels[self.config.LOG_LEVEL]
        self.web_client = web_client

    @property
    def uptime(self):
        return datetime.utcnow() - self.start_time

    async def setup_hook(self) -> None:
        # log.info("Setting up hook...")
        # log.info(f"Client user; {self.user} ({self.user.id})")
        # log.info(f"Client version; {self.version}")
        # log.info(f"Client Start Time; {self.start_time}")
        self.add_view(PersistentView())
        if self.testing_guild_id:
            # We'll copy in the global commands to test with:
            self.tree.copy_global_to(guild=self.testing_guild)
            # followed by syncing to the testing guild.
            await self.tree.sync(guild=self.testing_guild)
        else:  # We'll sync the global commands if we're not testing.
            # Sync the command tree to the client
            await self.tree.sync()

    # client.description = client.config.DESCRIPTION
    async def main(self):
        logger = getLogger("discord")
        logger.setLevel(self.log_level)
        file = RotatingFileHandler(
            filename="discord.log",
            encoding="utf-8",
            maxBytes=32 * 1024 * 1024,  # 32 MiB
            backupCount=5,  # Rotate through 5 files)
        )
        datetime_format = "%Y-%m-%d %H:%M:%S"
        formatter = Formatter(
            "[Time: {asctime}] {levelname:<8}\n(Path: {path})\n [Line: {lineno}] (Function: {funcName}) Logger: {name}\nMessage: {message}",
            datetime_format,
            style="{",
        )
        file.setFormatter(formatter)
        logger.addHandler(file)
        async with ClientSession() as session:
            async with FAQ_Client(
                web_client=session,
                intents=intents,
                case_insensitive=True,
                activity=Activity(
                    name=self.config.ACTIVITY, type=ActivityType.watching
                ),
                owner_ids=(
                    [owner_id for owner_id in self.config.OWNERS.strip().split(",")]
                    if self.config.OWNERS is not None
                    else []
                ),
            ) as client:
                # await client.setup_hook()
                await client.start(self.config.TOKEN)
