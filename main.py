from asyncio import run
from logging import INFO, FileHandler, Formatter, StreamHandler, basicConfig, getLogger
from typing import Optional, Tuple, Union

from discord import (
    Activity,
    ActivityType,
    Colour,
    Embed,
    Intents,
    Interaction,
    Member,
    User,
    app_commands,
)
from discord.ui import Button, View

from classes.dropdowns import AlphaDropdown
from classes.faq import FAQ_Client
from classes.persistent_view import PersistentView
from classes.structure import CustomEmbed
from topics import links

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


async def generate_dropdown(
    persistant: bool = False,
) -> Tuple[View, PersistentView, Embed]:
    if persistant is not True:
        view = View()
        view.add_item(AlphaDropdown())
        for link in links:
            view.add_item(
                Button(
                    label=link.label,
                    emoji=link.emoji,
                    url=link.url,
                    disabled=link.disabled,
                    row=link.row,
                )
            )

    elif persistant is True:
        view = PersistentView()

    embed = CustomEmbed(
        title="Welcome to the ModMail Help Center!",
        description="This is an **interactive FAQ** where you can find answers to common questions about ModMail. Use the Select Menu below to navigate through the FAQ.",
        colour=Colour.from_str(client.config.default_colour),
    )
    return view, embed


async def end_further_support(
    interaction: Interaction, user: Union[User, Member] = None
):
    await interaction.user.remove_roles(
        *[interaction.guild.get_role(int(Config().further_support_role))],
        reason="User no longer needs further support",
    )
    await interaction.response.send_message(
        f"You have been removed the {interaction.guild.get_role(int(Config().further_support_role)).mention} role to gain access to the further support channel.",
        ephemeral=True,
    )


@client.tree.command(name="faq", description="Get support for ModMail")
async def faq(interaction: Interaction):
    view, embed = await generate_dropdown()
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


@client.tree.command(name="post", description="Post the standalone help menu")
@app_commands.describe(ephemeral="Accepts 'True' or 'False")
async def post(interaction: Interaction, ephemeral: Optional[bool] = False):
    view, embed = await generate_dropdown(persistant=True)
    await interaction.response.send_message(embed=embed, view=view, ephemeral=ephemeral)


@client.tree.command(name="help", description="Get support for ModMail")
async def help(interaction: Interaction):
    view, embed = await generate_dropdown()
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


@client.tree.command(
    name="remove", description="Remove a user from the further support role"
)
async def remove(interaction: Interaction):
    await interaction.response.send_message("This command is not yet implemented.")


@client.tree.context_menu(
    name="remove",
)
async def remove(interaction: Interaction, user: Union[User, Member]):
    await interaction.response.send_message("This command is not yet implemented.")


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
