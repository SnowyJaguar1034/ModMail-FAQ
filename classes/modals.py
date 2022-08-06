from logging import getLogger

from discord import Interaction, TextStyle
from discord.ui import Modal, TextInput

from classes.structure import CustomEmbed

log = getLogger(__name__)


class CustomInstanceRequest(Modal, title="Custom Instance Request"):
    def __init__(
        self, attachment, channel, custom_id: str = "CustomInstanceRequest"
    ) -> None:
        self.attachment = attachment
        self.channel = channel

    # Our modal classes MUST subclass `discord.ui.Modal`,
    # but the title can be whatever you want.

    # This will be a short input, where the user can enter their name
    # It will also have a placeholder, as denoted by the `placeholder` kwarg.
    # By default, it is required and is a short-style input which is exactly
    # what we want.
    name = TextInput(
        label="Bot Name",
        placeholder="Your bot name here...\nDefault: ModMail\n(optional)",
        min_length=1,
        max_length=32,
        default="ModMail",
        required=False,
    )

    activity = TextInput(
        label="Bot status activity",
        placeholder="Your bot status here...\nDefault: DM to Contact Staff | =help\n(optional)",
        max_length=128,
        default="DM to Contact Staff | =help",
        required=False,
    )

    about_me = TextInput(
        label="Bot About Me",
        placeholder="Your bot about me here...\n(optional)",
        max_length=400,
        required=False,
    )

    server = TextInput(
        label="Bot Server",
        placeholder="Your bot server here...\n(required)",
    )

    # This is a longer, paragraph style input, where user can submit feedback
    # Unlike the name, it is not required. If filled out, however, it will
    # only accept a maximum of 300 characters, as denoted by the
    # `max_length=300` kwarg.
    customizations = TextInput(
        label="What other customizations would you like? If any",
        style=TextStyle.long,
        placeholder="Type your requests here...",
        required=False,
        max_length=300,
    )

    async def on_submit(self, interaction: Interaction):
        embed = CustomEmbed(title="Custom Instance Application")
        embed.add_field(
            name="User",
            value=f"{interaction.user.mention} ({interaction.user.id})",
        )
        embed.add_field(
            name="Attachment",
            value=f"{self.attachment.filename} ({self.attachment.size} bytes)",
        )
        embed.set_footer(text="Sent via FAQ")
        await self.channel.send(embed=embed)
        await interaction.response.send_message(
            f"Thanks for your instance request, {interaction.user.display_name}!",
            ephemeral=True,
        )

    async def on_error(self, interaction: Interaction, error: Exception) -> None:
        await interaction.response.send_message(
            "Oops! Something went wrong.", ephemeral=True
        )

        # Make sure we know what the error actually is
        # traceback.print_tb(error.__traceback__)
        log.error(f"{error.__class__.__name__}: {error}")
