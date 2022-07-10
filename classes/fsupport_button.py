from logging import getLogger

from discord import ButtonStyle, Colour, Embed, Forbidden, HTTPException, Interaction
from discord.ui import Button, View

from classes.config import Config

log = getLogger(__name__)


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
        embed = Embed(
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
        role = interaction.guild.get_role(int(Config().further_support_role))
        if role is None:
            log.error(
                f"Could not find a role with ID '{Config().further_support_role_id}', it's returning 'None'"
            )
            return
        try:
            await interaction.user.add_roles(
                *[role], reason="User requested further support"
            )
        except Forbidden as e:
            log.error(
                f"Could not remove '{role.name}' from '{interaction.user.name}', bot has insufficient permissions\n{e}"
            )
        except HTTPException as e:
            log.error(
                f"Could not remove '{role.name}' from '{interaction.user.name}', adding the roles failed\n{e}"
            )
        await interaction.response.send_message(
            f"You have been given the {role.mention} role to gain access to the further support channel.",
            ephemeral=True,
        )
