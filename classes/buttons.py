from logging import getLogger

from discord import ButtonStyle, Colour, Interaction, PartialEmoji
from discord.ui import Button, View
from further_support import further_support
from topics import rules

from classes.config import Config
from classes.structure import CustomEmbed

log = getLogger(__name__)


class Credits(Button):
    def __init__(self, custom_id: str = "Credits") -> None:
        super().__init__(
            label="Credits",
            style=ButtonStyle.blurple,
            custom_id=custom_id,
            row=2,
        )

    async def callback(self, interaction: Interaction):
        view = View()
        view.add_item(
            Button(
                label="Join the Icons Server",
                url=Config().ICONS_SERVER_URL,
                emoji="<:IconsServerCredit:995423046397599764>",
            )
        )
        embed = CustomEmbed(
            title="Credits",
            description="Thank you for the Icons server for giving us permission to use their lovely icons within our support system. Want to use these own icons in your own server? Join the Icons server to find out how!",
            colour=Colour.orange(),
            url=Config().ICONS_SERVER_URL,
        )
        embed.set_thumbnail(
            url=PartialEmoji.from_str("<:IconsServerCredit:995423046397599764>").url,
        )
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


class Rules(Button):
    def __init__(self, custom_id: str = "Rules") -> None:
        super().__init__(
            label="Rules",
            style=ButtonStyle.blurple,
            custom_id=custom_id,
            row=2,
            emoji="<:icons_rules:999068968025337977>",
        )

    async def callback(self, interaction: Interaction):
        view = View()
        embed = CustomEmbed()
        for rule in rules.options:
            embed.add_field(
                name=f"{rule.id}. {rule.label}",
                value=rule.content,
                inline=False,
            )
            if rule.links:
                for link in rule.links:
                    view.add_item(
                        Button(label=link.label, url=link.url, emoji=link.emoji)
                    )
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


class FSupportButton(Button):
    def __init__(self, custom_id: str = "Further-Support") -> None:
        super().__init__(
            label="I couldn't find what I'm looking for!",
            style=ButtonStyle.blurple,
            custom_id=custom_id,
            emoji="<:ICouldntFindWhatImLookingFor:995421072340037725>",
            row=2,
        )

    async def callback(self, interaction: Interaction):
        view = View()
        view.add_item(RoleAdd())
        embed = CustomEmbed(
            title="Further Support Confirmation",
            description="I understand that moderation action will be taken against me if my question was answered in the FAQ",
            colour=Colour.orange(),
        )
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


class RoleAdd(Button):
    def __init__(self, custom_id: str = "fsupport_button") -> None:
        super().__init__(
            label="I Understand",
            style=ButtonStyle.green,
            custom_id=custom_id,
            emoji="📩",
            row=2,
        )

    async def callback(self, interaction: Interaction):
        # get the further support role from the clients cache
        await further_support(
            action="add",
            user=interaction.user,
            role=interaction.guild.get_role(int(Config().FURTHER_SUPPORT_ROLE)),
            response=interaction.response,
        )
