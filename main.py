import asyncio
from logging import (
    INFO,
    WARNING,
    FileHandler,
    Formatter,
    StreamHandler,
    basicConfig,
    getLogger,
)

from discord import Activity, ActivityType, Embed, Intents, Interaction
from discord.ext import commands

from classes.dropdown import AlphaDropdownView
from classes.faq import FAQ_Client

intents = Intents.default()
intents.message_content = True

client = FAQ_Client(
    intents=intents,
    owner_ids=["Owners"],
    command_prefix=commands.when_mentioned,
    case_insensitive=True,
)
client.activity = Activity(name=client.config.activity, type=ActivityType.watching)
client.description = client.config.description

basicConfig(level=INFO)
logger = getLogger()
file = FileHandler(filename="faq.log", encoding="utf-8", mode="w")
file.setFormatter(
    Formatter(
        """
      Time: %(asctime)s: 
      Level: %(levelname)s: 
      Logger: %(name)s: 
      Path: %(pathname)s: 
      Line: %(lineno)d:
      Function: %(funcName)s:
      Message: %(message)s
      """
    )
)
logger.addHandler(file)

log = getLogger(__name__)

data_loaded = None


@client.tree.command()
async def faq(interaction: Interaction):
    view = AlphaDropdownView()
    embed = Embed(
        title="Welcome to the ModMail Help Center!",
        description='This is an **interactive FAQ** where you can find answers to common questions about ModMail. Use the Select Menu below to navigate through the FAQ. You can go back to the previous topic by clicking the "Back" button',
    )
    await interaction.response.send_message(embed=embed, view=view)


if __name__ == "__main__":
    asyncio.run(client.main())
