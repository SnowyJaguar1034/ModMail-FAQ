from logging import getLogger
from typing import Optional

from discord import ButtonStyle, Embed, Interaction, PartialEmoji, SelectOption
from discord.ui import Button, Select, View
from topics import initial
from utils.mappings import mainoptions_mapping, suboption_mapping

from classes.config import Config
from classes.fsupport_button import FSupportButton

from .structure import CustomEmbed, SubOptions

log = getLogger(__name__)


# Defines the main dropdown select menu for the FAQ
class AlphaDropdown(Select):
    def __init__(self, custom_id: str = "base_alphadropdown") -> None:
        options = [
            SelectOption(
                label=article.label,
                description=article.description,
                emoji=article.emoji,
                value=str(article.id),
            )
            for article in initial.articles
        ]
        options.append(
            SelectOption(
                label="I couldn't find what I'm looking for!",
                value=Config().FURTHER_SUPPORT_ROLE,
                emoji="<:ICouldntFindWhatImLookingFor:995421072340037725>",
            )
        )

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(
            placeholder="Select a topic...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id=custom_id,
        )

    async def callback(self, interaction: Interaction) -> None:
        # Get the selected option and check if it's a request for further suppor, if it is send the confirmation and stop menu
        if self.values[0] == Config().FURTHER_SUPPORT_ROLE:
            await FSupportButton().callback(interaction)
            return

        # Figure out the corresponding article to their selection
        # elif float(self.values[0]) == 1.0:
        #     menu = initial.articles[0]
        # elif float(self.values[0]) == 2.0:
        #     menu = initial.articles[1]
        # elif float(self.values[0]) == 3.0:
        #     menu = initial.articles[2]
        # elif float(self.values[0]) == 4.0:
        #     menu = initial.articles[3]
        # elif float(self.values[0]) == 5.0:
        #     menu = initial.articles[4]

        for key in mainoptions_mapping.keys():
            if float(self.values[0]) == key:
                menu = initial.articles[int(key) - 1]

        embed = CustomEmbed(
            title=menu.label,
            description=f"{menu.description}\n\n{menu.content}",
        )

        # Figure out the sub-questions to display
        options_to_show = suboption_mapping.get(float(self.values[0]))

        # Adds each sub question to the select menu options
        next_options: list[SelectOption] = [
            SelectOption(
                label=question.label,
                emoji=question.emoji,  # PartialEmoji.from_str() if question.emoji else None,
            )
            for question in options_to_show.options
        ]

        # Create a View object and generate the embed with the sub-questions
        view = View()
        view.add_item(BetaDropdown(options_to_show, next_options))
        for article in options_to_show.options:
            embed.add_field(
                name=article.label,
                value=article.description if article.description else "\u200b",
                inline=False,
            )
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


# Defines the sub dropdown for the selected FAQ option
class BetaDropdown(Select):
    def __init__(
        self,
        sub_option: Optional[SubOptions],
        options: list[SelectOption],
    ):
        self.sub_option = sub_option
        super().__init__(
            placeholder="Select a question...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: Interaction) -> None:
        embed = CustomEmbed(title=self.values[0])

        for question in self.sub_option.options:
            # Figure out which sub question was chosen and get the content (answer) of the question
            if question.label == self.values[0]:  # .value
                embed.description = question.content

                if question.image:
                    embed.set_image(url=question.image)

                view = View()
                if question.links:
                    for link in question.links:
                        view.add_item(
                            Button(label=link.label, url=link.url, emoji=link.emoji)
                        )
                view.add_item(FSupportButton())

        await interaction.response.send_message(embed=embed, ephemeral=True, view=view)
