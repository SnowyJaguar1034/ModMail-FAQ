from datetime import datetime
from logging import (
    CRITICAL,
    DEBUG,
    ERROR,
    INFO,
    WARNING,
    Formatter,
    StreamHandler,
    getLogger,
)
from logging.handlers import RotatingFileHandler, SMTPHandler

from aiohttp import ClientSession
from discord import Activity, ActivityType, Client, Intents, Object, app_commands
from mappings import activities, log_levels

from classes.config import Config
from classes.custom_smtphandler import HTMLSMTPHandler
from classes.log_colour_filter import CustomFilter
from classes.views import PersistentView

intents = Intents.default()
intents.message_content = True
intents.members = True
intents.emojis = True

config = Config().load()

datetime_format = "%Y-%m-%d %H:%M:%S"
logger = getLogger("discord")
logger.setLevel(log_levels[Config().LOG_LEVEL])
file = RotatingFileHandler(
    filename="discord.log",
    encoding="utf-8",
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files)
)
console = StreamHandler()
email = HTMLSMTPHandler(
    mailhost=(Config().MAIL_HOST, Config().MAIL_PORT),
    fromaddr=Config().MAIL_FROM,
    toaddrs=Config().RECIPIENTS.strip(" ").split(","),  # recipients,
    subject=Config().MAIL_SUBJECT or f"FAQ encountered an error",
    credentials=(Config().MAIL_USER, Config().MAIL_PASS),
    secure=(),
    timeout=Config().MAIL_TIMEOUT,
    type="HTML",
)
formatter = Formatter(
    "---------------\n[Time: {asctime}] {levelname}\n(Path: {pathname})\n[Line: {lineno}] (Function: {funcName}) Logger: {name}\nMessage: {message}\n---------------\n",
    datetime_format,
    style="{",
)
email.addFilter(CustomFilter())
email_formatter = Formatter(
    """\
    <html>
    <head>
    <style>body </style>
    </head>
    <body>
    <h1>FAQ encountered an error</h1>
    <p>Time: {asctime}</p>
    <p>Level: {levelname}</p>
    <p>Path: {pathname}</p>
    <p>Line: {lineno}</p>
    <p>Function: {funcName}</p>
    <p>Logger: {name}</p>
    <p>Message: {message}</p>
    </body>
    </html>""",
    datetime_format,
    style="{",
)
file.setFormatter(formatter)
console.setFormatter(formatter)
email.setFormatter(email_formatter)
logger.addHandler(file)
logger.addHandler(console)
logger.addHandler(email)


class FAQ_Client(Client):
    def __init__(self, web_client: ClientSession = None, *args, **kwargs):
        super().__init__(**kwargs)
        self.start_time = datetime.utcnow()
        self.tree = app_commands.CommandTree(self)
        self.config = config
        self.testing_guild = Object(self.config.TESTING_GUILD)
        self.version = self.config.VERSION
        self.log_level = log_levels[self.config.LOG_LEVEL]
        self.web_client = web_client

    @property
    def uptime(self):
        return datetime.utcnow() - self.start_time

    async def setup_hook(self) -> None:
        logger.info(
            f"Setting up hook...\nClient user; {self.user} ({self.user.id})\nClient version; {self.version}\nClient Start Time; {self.start_time}"
        )
        logger.debug("Example of a DEBUG log")
        logger.info("Example of an INFO log")
        logger.warning("Example of a WARNING log")
        logger.error("Example of an ERROR log")
        logger.critical("Example of a CRITICAL log")
        logger.info("Setting up persistent views...")
        self.add_view(PersistentView())
        if self.testing_guild:
            # We'll copy in the global commands to test with:
            try:
                self.tree.copy_global_to(guild=self.testing_guild)
                logger.info(
                    f"Copying global commands to test guild {Config().TESTING_GUILD}"
                )
            except Exception as e:
                logger.error(
                    f"Error copying global commands to test guild {Config().TESTING_GUILD}:\n{e.message}"
                )
            # followed by syncing to the testing guild.
            try:
                await self.tree.sync(guild=self.testing_guild)
                logger.info(
                    f"Syncing global commands to test guild {Config().TESTING_GUILD}"
                )
            except Exception as e:
                logger.error(
                    f"Error syncing global commands to test guild {Config().TESTING_GUILD}:\n{e.message}"
                )
        else:  # We'll sync the global commands if we're not testing.
            # Sync the command tree to the client
            try:
                await self.tree.sync()
                logger.info("Syncing global commands")
            except Exception as e:
                logger.error(f"Error syncing global commands:\n{e.message}")

    async def main(self):
        async with ClientSession() as session:
            async with FAQ_Client(
                web_client=session,
                intents=intents,
                case_insensitive=True,
                activity=Activity(
                    name=Config().ACTIVITY, type=activities[Config().ACTIVITY_TYPE]
                ),
                owner_ids=(
                    [owner_id for owner_id in Config().OWNERS.strip().split(",")]
                    if Config().OWNERS is not None
                    else []
                ),
            ) as client:
                await client.start(Config().TOKEN)
