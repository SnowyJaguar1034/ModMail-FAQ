from logging import getLogger

from discord import ButtonStyle, Embed, Interaction, PartialEmoji, SelectOption
from discord.ui import Button, Select, View
from topics import initial
from utils.mappings import mainoptions_mapping, suboption_mapping

from classes.config import Config
from classes.fsupport_button import FSupportButton

from .structure import CustomEmbed

log = getLogger(__name__)


# Defines a custom Select containing colour options that the user can choose. The callback function of this class is called when the user changes their choice
class AlphaDropdown(Select):
    def __init__(self, custom_id: str = "base_alphadropdown") -> None:
        options = [
            SelectOption(
                label=article.label,
                description=article.description,
                emoji=article.emoji,  # PartialEmoji.from_str() if article.emoji else None,
                value=str(article.id),
            )
            for article in initial.articles
        ]
        options.append(
            SelectOption(
                label="I couldn't find what I'm looking for!",
                value=Config().further_support_role,
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

    async def callback(self, interaction: Interaction):
        # Figure out the corresponding article to their selection

        # Gets the select option that was clicked on
        if self.values[0] == Config().further_support_role:
            await FSupportButton().callback(interaction)
            return
        elif float(self.values[0]) == 1.0:
            menu = initial.articles[0]
        elif float(self.values[0]) == 2.0:
            menu = initial.articles[1]
        elif float(self.values[0]) == 3.0:
            menu = initial.articles[2]
        elif float(self.values[0]) == 4.0:
            menu = initial.articles[3]
        elif float(self.values[0]) == 5.0:
            menu = initial.articles[4]

        embed = CustomEmbed(
            title=menu.label,
            description=f"{menu.description}\n{menu.content}",
            colour=menu.colour,
        )
        # embed.set_footer(
        #     text=credits.text, icon_url=PartialEmoji.from_str(credits.emoji).url
        # )

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
        embed = CustomEmbed(
            title=mainoptions_mapping[float(self.values[0])],
            description="\n\n".join(
                [f"**{article.label}**" for article in options_to_show.options]
            ),
            colour=menu.colour,
        )
        # embed.set_footer(
        #     text=credits.text, icon_url=PartialEmoji.from_str(credits.emoji).url
        # )
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


# Defines a custom Select containing colour options that the user can choose. The callback function of this class is called when the user changes their choice
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
        embed = CustomEmbed(title=self.values[0])
        # embed.set_footer(
        #     text=credits.text, icon_url=PartialEmoji.from_str(credits.emoji).url
        # )
        for question in self.sub_option.options:
            embed.color = question.colour
            # Figure out which sub question was chosen and get the content (answer) of the question
            if question.label == self.values[0]:  # .value
                embed.description = question.content
                embed.colour = question.colour

                if question.image:
                    embed.set_image(url=question.image)

                view = View()
                if question.links:
                    for link in question.links:
                        view.add_item(Button(label=link.label, url=link.url))
                view.add_item(FSupportButton())

        await interaction.response.send_message(embed=embed, ephemeral=True, view=view)
