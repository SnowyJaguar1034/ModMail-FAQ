from logging import getLogger

from discord.ui import Button, View, button

from classes.buttons import Credits, Rules
from classes.dropdowns import AlphaDropdown
from topics import links

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
        self.add_item(Credits())
        self.add_item(Rules())


class VolatileView(View):
    def __init__(self):
        super().__init__()
        # Add the base dropdown to the view
        self.add_item(AlphaDropdown())
        # Loop through the links and add them to the view
        for link in links:
            self.add_item(
                Button(
                    label=link.label,
                    url=link.url,
                    emoji=link.emoji,
                )
            )
        self.add_item(Credits())
        self.add_item(Rules())
