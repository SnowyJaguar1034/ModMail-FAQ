from asyncio import run
from logging import INFO, FileHandler, Formatter, StreamHandler, basicConfig, getLogger
from typing import Optional, Union

from discord import (
    Activity,
    ActivityType,
    Attachment,
    Intents,
    Interaction,
    Member,
    User,
    app_commands,
)
from discord.app_commands import Group

from classes.faq import FAQ_Client  # main
from classes.modals import CustomInstanceRequest
from further_support import further_support
from utils import generate_dropdown, is_bot_owner

log = getLogger(__name__)

intents = Intents.default()
intents.message_content = True
intents.members = True
intents.emojis = True

client = FAQ_Client(
    intents=intents,
)
# client.activity = Activity(name=client.config.ACTIVITY, type=ActivityType.watching)
# # client.description = client.config.DESCRIPTION
# client.owner_ids = (
#     [owner_id for owner_id in client.config.OWNERS.strip().split(",")]
#     if client.config.OWNERS is not None
#     else []
# )
# client.case_insensitive = True


@is_bot_owner()
@client.tree.command(name="post", description="Post the standalone help menu")
@app_commands.describe(ephemeral="Accepts 'True' or 'False")
async def post(interaction: Interaction, ephemeral: Optional[bool] = False):
    if interaction.user.id not in client.owner_ids:
        return await interaction.response.send_message(
            "You do not have permission to use this command.",
            ephemeral=True,
        )
    view, embed = await generate_dropdown(
        default_colour=client.config.DEFAULT_COLOUR, persistant=True
    )
    await interaction.response.send_message(embed=embed, view=view, ephemeral=ephemeral)


@client.tree.command(name="faq", description="Get support for ModMail")
async def faq(interaction: Interaction):
    view, embed = await generate_dropdown(
        defauult_colour=client.config.DEFAULT_COLOUR, persistant=False
    )
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


@client.tree.command(name="help", description="Get support for ModMail")
async def help(interaction: Interaction):
    view, embed = await generate_dropdown(
        defauult_colour=client.config.DEFAULT_COLOUR, persistant=False
    )
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


@client.tree.command(
    name="custom",
    description="Apply for a custom instance of ModMail",
)
@app_commands.describe(attachment="The profile picture you want for your bot")
async def custom_instance_application(
    interaction: Interaction, attachment: Attachment = None
):
    channel = client.get_channel(int(client.config.INSTANCE_REQUESTS))
    await interaction.response.send_modal(
        CustomInstanceRequest(attachment=attachment, channel=channel)
    )
    # await interaction.followup(
    #     "Your application has been submitted, you will be contacted shortly.",
    #     ephemeral=True,
    # )


# @client.tree.command(
#     name="private-instances",
#     description="Shows a list of all the private instances hosted by James",
# )
# async def private_instances(interaction: Interaction):
#     # bots is a dictioniry of bot ID to bot name and bot owner
#     bots = {}
#     ignored = [
#         859584658676383754,  # Go Postal
#         941314754851524639,  # Zupie
#         986757903090327552,  # FAQ
#         933684530026545193,  # Elf
#         799403868534079509,  # Alpha
#         575252669443211264,  # Modmail
#         692547870183915618,  # Syndicate
#         699033133550665788,  # Modmail Beta
#         785360543665487874,  # ModMail Alpha
#     ]
#     pages = []
#     hosted = client.get_guild(607652789304164362)
#     for member in hosted.members:
#         if member.bot:
#             if member.id not in ignored:
#                 bots[member.id] = member.name

#     embed = Embed(title="Private Instances")
#     embed2 = Embed(title="Private Instances")
#     for bot in bots:
#         if len(embed.fields) <= 24:
#             embed.add_field(name=bot, value=bots[bot])
#         elif len(embed.fields) > 24:
#             embed2.add_field(name=bots[bot], value=bot)

#     pages.append(embed)
#     pages.append(embed2)

#     await interaction.response.send_message(embeds=pages, ephemeral=True)

end = Group(name="end", description="Remove a user from the further support role")
further = Group(
    name="further",
    parent=end,
    description="Remove a user from the further support role",
)


@further.command(
    name="support",
    description="Remove a user from the further support role",
)
async def support(interaction: Interaction, user: Union[User, Member] = None):
    await further_support(
        action="remove",
        user=user or interaction.user,
        role=interaction.guild.get_role(int(client.config.FURTHER_SUPPORT_ROLE)),
        response=interaction.response,
    )


@client.tree.context_menu(
    name="End Further Support",
)
async def remove(interaction: Interaction, user: Union[User, Member]):
    await further_support(
        action="remove",
        user=user or interaction.user,
        role=interaction.guild.get_role(int(client.config.FURTHER_SUPPORT_ROLE)),
        response=interaction.response,
    )


client.tree.add_command(end)

if __name__ == "__main__":
    run(client.main())
