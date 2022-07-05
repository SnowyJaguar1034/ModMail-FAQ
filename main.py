from asyncio import run
from logging import INFO, FileHandler, Formatter, StreamHandler, basicConfig, getLogger
from typing import Optional

from discord import (
    Activity,
    ActivityType,
    Colour,
    Embed,
    Intents,
    Interaction,
    app_commands,
)
from discord.ext import commands
from discord.ui import Button, View

from classes.dropdown import AlphaDropdown, PersistentDropdown
from classes.faq import FAQ_Client
from classes.topics import links

intents = Intents.default()
intents.message_content = True
intents.members = True
intents.emojis = True

client = FAQ_Client(
    intents=intents,
)
client.activity = Activity(name=client.config.activity, type=ActivityType.watching)
client.description = client.config.description
client.owner_ids = (
    [owner_id for owner_id in client.config.owners.strip().split(",")]
    if client.config.owners is not None
    else []
)
client.case_insensitive = True
client.command_prefix = commands.when_mentioned_or("!")

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


async def generate_dropdown(
    interaction: Interaction,
    ephemeral: Optional[bool] = False,
    persistant: Optional[bool] = False,
):
    view = View()

    for link in links:
        button = Button(label=link.label, emoji=link.emoji, url=link.url)
        view.add_item(button)
    if persistant is not True:
        view.add_item(AlphaDropdown())
    elif persistant is True:
        view.add_item(PersistentDropdown())
    embed = Embed(
        title="Welcome to the ModMail Help Center!",
        description='This is an **interactive FAQ** where you can find answers to common questions about ModMail. Use the Select Menu below to navigate through the FAQ. You can go back to the previous topic by clicking the "Back" button',
        colour=Colour.from_str(client.config.default_colour),
    )
    await interaction.response.send_message(embed=embed, view=view, ephemeral=ephemeral)


@client.tree.command(name="faq", description="Get support for ModMail")
async def faq(interaction: Interaction):
    await generate_dropdown(interaction=interaction)


@client.tree.command(name="post", description="Post the standalone help menu")
@app_commands.describe(ephemeral="Accepts 'True' or 'False")
async def post(interaction: Interaction, ephemeral: Optional[bool] = False):
    await generate_dropdown(
        interaction=interaction, ephemeral=ephemeral, persistant=True
    )


@client.tree.command(
    name="private-instances",
    description="Shows a list of all the private instances hosted by James",
)
async def private_instances(interaction: Interaction):
    # bots is a dictioniry of bot ID to bot name and bot owner
    bots = {}
    ignored = [
        859584658676383754,  # Go Postal
        941314754851524639,  # Zupie
        986757903090327552,  # FAQ
        933684530026545193,  # Elf
        799403868534079509,  # Alpha
        575252669443211264,  # Modmail
        692547870183915618,  # Syndicate
        699033133550665788,  # Modmail Beta
        785360543665487874,  # ModMail Alpha
    ]
    pages = []
    hosted = client.get_guild(607652789304164362)
    for member in hosted.members:
        if member.bot:
            if member.id not in ignored:
                bots[member.id] = member.name

    embed = Embed(title="Private Instances")
    embed2 = Embed(title="Private Instances")
    for bot in bots:
        if len(embed.fields) <= 24:
            embed.add_field(name=bot, value=bots[bot])
        elif len(embed.fields) > 24:
            embed2.add_field(name=bots[bot], value=bot)

    pages.append(embed)
    pages.append(embed2)

    await interaction.response.send_message(embeds=pages, ephemeral=True)


if __name__ == "__main__":
    run(client.main())
