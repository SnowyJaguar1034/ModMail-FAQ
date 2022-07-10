from logging import getLogger

from discord import ButtonStyle, Embed, HTTPException, Interaction
from discord.ui import Button, View, button
from topics import links

from classes.config import Config
from classes.dropdowns import AlphaDropdown
from classes.fsupport_button import FSupportButton

log = getLogger(__name__)


class PersistentView(View):
    def __init__(self):
        super().__init__(timeout=None)
        # Add the base dropdown to the view
        self.add_item(AlphaDropdown(custom_id="persistent_dropdown"))
        # Loop through the links and add them to the view
        for link in links:
            self.add_item(
                Button(
                    label=link.label,
                    url=link.url,
                    emoji=link.emoji,
                )
            )
