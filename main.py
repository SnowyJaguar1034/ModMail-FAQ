import asyncio
import json
import logging
import traceback
from logging import INFO, FileHandler, Formatter, StreamHandler, basicConfig, getLogger
from logging.handlers import SMTPHandler
from os import environ
from typing import Optional

import yaml
from discord import Activity, ActivityType, Embed, Intents, Interaction
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import format_dt

from config import Config
from dropdown import AlphaDropdownView
from faq import FAQ_Client
from tbd import FAQ_Group

config = Config().load()

intents = Intents.default()
intents.message_content = True

print(f"Token: {Config().TOKEN}")

client = FAQ_Client(
    intents=intents,
    activity=Activity(name=Config().ACTIVITY, type=ActivityType.watching),
    owner_ids=["Owners"],
    description=Config().DESCRIPTION,
    command_prefix=commands.when_mentioned,
    case_insensitive=True,
)

# client.tree.add_command(FAQ_Group(client))

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
# console = StreamHandler()
# console.setLevel(INFO)
# console.setFormatter(
#     Formatter("%(asctime)s: %(levelname)s: %(name)s: (%(funcName)): %(message)s")
# )
logger.addHandler(file)
# logger.addHandler(console)

log = getLogger(__name__)

data_loaded = None


@client.tree.command()
async def faq(interaction: Interaction):
    """Sends a message with our dropdown containing colours"""

    # Create the view containing our dropdown
    view = AlphaDropdownView()
    embed = Embed(
        title="Welcome to the ModMail Help Center!",
        description='This is an **interactive FAQ** where you can find answers to common questions about ModMail. Use the Select Menu below to navigate through the FAQ. You can go back to the previous topic by clicking the "Back" button',
    )
    # Sending a message containing our view
    await interaction.response.send_message(embed=embed, view=view)


print(f"Uptime: {client.uptime} seconds elapsed")


if __name__ == "__main__":
    asyncio.run(client.main())
