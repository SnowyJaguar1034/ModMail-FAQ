from logging import getLogger
from typing import Tuple

from discord import Colour, Embed, Interaction, app_commands
from discord.ui import View

from classes.structure import CustomEmbed
from classes.views import PersistentView, VolatileView

log = getLogger(__name__)


def is_bot_owner():
    def predicate(interaction: Interaction) -> bool:
        if interaction.user.id in client.owner_ids:
            return True

    return app_commands.check(predicate)


async def generate_dropdown(
    default_colour: str,
    persistant: bool = False,
) -> Tuple[View, PersistentView, Embed]:
    view = PersistentView() if persistant is True else VolatileView()

    embed = CustomEmbed(
        title="Welcome to the ModMail Help Center!",
        description="This is an **interactive FAQ** where you can find answers to common questions about ModMail. Use the Select Menu below to navigate through the FAQ.\n\n> - If your having issues with ModMail as a user, like not being able to DM ModMail, select `Common Troubleshooting for Users`\n> - If your having issues with ModMail as a staff member, like which permissions ModMail needs, select `Common troubleshooting for Staff`\n> - If your having issues with ModMail premium, kike not receiving your patron role, select `Common Issues with Purchasing Premium`\n> - If your looking for a list of commands then select `How do I use X command`\n> - If you cannot find what your are looking for, select 'I can't find what I'm looking for!`",
        colour=Colour.from_str(defauult_colour),
    )
    return view, embed
