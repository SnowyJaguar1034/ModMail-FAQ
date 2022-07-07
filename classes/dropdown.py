from logging import getLogger
from typing import Union

from discord import Embed, Interaction, SelectOption
from discord.ui import Button, Select, View

from classes import topics
from classes.topics import aspects, how_to_commands, initial, premium, trouleshooting

log = getLogger(__name__)


# Defines a custom Select containing colour options that the user can choose. The callback function of this class is called when the user changes their choice
class AlphaDropdown(Select):
    def __init__(self, custom_id: str = "base_alphadropdown") -> None:
        self.custom_id = custom_id
        options = [
            SelectOption(
                label=article.label,
                description=article.description,
                emoji=article.emoji,  # PartialEmoji.from_str() if article.emoji else None,
                value=str(article.id),
            )
            for article in topics.initial.articles
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(
            placeholder="Select a topic...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id=self.custom_id,
        )

    async def callback(self, interaction: Interaction):
        # Figure out the corresponding article to their selection

        # Gets the select option that was clicked on
        if float(self.values[0]) == 1.0:
            menu = initial.articles[0]
        elif float(self.values[0]) == 2.0:
            menu = initial.articles[1]
        elif float(self.values[0]) == 3.0:
            menu = initial.articles[2]
        elif float(self.values[0]) == 4.0:
            menu = initial.articles[3]
        elif float(self.values[0]) == 5.0:
            menu = initial.articles[4]

        embed = Embed(
            title=menu.label,
            description=f"{menu.description}\n{menu.content}",
            colour=menu.colour,
        )

        # Get the list of sub-questions to display, based on their selection

        suboption_mapping = {
            1.0: trouleshooting,
            2.0: aspects,
            3.0: premium,
            4.0: how_to_commands,
        }

        # Figure out the sub-questions to display
        options_to_show = suboption_mapping.get(float(self.values[0]))

        # Adds each sub question to the select menu options
        next_options: list[SelectOption] = [
            SelectOption(
                label=question.label,
            )
            for question in options_to_show.options
        ]

        # Create a View object and generate the embed with the sub-questions
        view = View()
        view.add_item(BetaDropdown(options_to_show, next_options))
        embed = Embed(
            title=self.values[0],
            description="\n\n".join(
                [f"**{article.label}**" for article in options_to_show.options]
            ),
        )
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


class BetaDropdown(Select):
    def __init__(
        self,
        sub_option,
        options: list[SelectOption],
    ):
        self.sub_option = sub_option
        super().__init__(
            placeholder="Select a question...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: Interaction):
        embed = Embed(title=self.values[0])
        for question in self.sub_option.options:

            # Figure out which sub question was chosen and get the content (answer) of the question
            if question.label == self.values[0]:  # .value
                embed.description = question.content
                embed.colour = question.colour

                if question.image:
                    embed.set_image(url=question.image)

                view = View()
                if question.links:
                    url_buttons = []
                    for (
                        key,
                        value,
                    ) in question.links.items():  # Iterating through the dictionary
                        url_buttons.append(
                            Button(label=key, url=value)
                        )  # Create button(s) that redirect to a link.

                    for button in url_buttons:
                        view.add_item(button)

        await interaction.response.send_message(embed=embed, ephemeral=True, view=view)


class PersistentDropdown(AlphaDropdown):
    def __init__(self):
        super().__init__(custom_id="persistent_dropdown")
