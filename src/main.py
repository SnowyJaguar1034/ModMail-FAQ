from typing import Optional

from discord import app_commands, Client, Intents, Object, Interaction, Member, Message, ButtonStyle, Embed, ui
import discord.utils as disutils

import asyncio
import logging
import logging.config

import msgspec

logger = logging.getLogger(__name__)

MAIN_GUILD = Object(id=0)  # replace with your guild id

decoder = msgspec.yml.Decoder()
encoder = msgspec.yml.Encoder()

with open("response_mapping.yml", "r") as f:
    RESPONSE_MAPPING = decoder.load(f)


class MyClient(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command state required to make it work.
        # This is a separate class because it allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MAIN_GUILD)
        await self.tree.sync(guild=MAIN_GUILD)


intents = Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
async def hello(interaction: Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')


@client.tree.command()
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
async def add(interaction: Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')


# The rename decorator allows us to change the display of the parameter on Discord.
# In this example, even though we use "text_to_send" in the code, the client will use "text" instead.
# Note that other decorators will still refer to it as "text_to_send" in the code.
@client.tree.command()
@app_commands.rename(text_to_send='text')
@app_commands.describe(text_to_send='Text to send in the current channel')
async def send(interaction: Interaction, text_to_send: str):
    """Sends the text into the current channel."""
    await interaction.response.send_message(text_to_send)


# To make an argument optional, you can either give it a supported default argument
# or you can mark it as Optional from the typing standard library. This example does both.
@client.tree.command()
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
async def joined(interaction: Interaction, member: Optional[Member] = None):
    """Says when a member joined."""
    # If no member is explicitly provided then we use the command user here
    member = member or interaction.user

    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member} joined {disutils.format_dt(member.joined_at)}')


# A Context Menu command is an app command that can be run on a member or on a message by
# accessing a menu within the client, usually via right clicking.
# It always takes an interaction as its first parameter and a Member or Message as its second parameter.

# This context menu command only works on members
@client.tree.context_menu(name='Show Join Date')
async def show_join_date(interaction: Interaction, member: Member):
    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member} joined at {disutils.format_dt(member.joined_at)}')


# This context menu command only works on messages
@client.tree.context_menu(name='Report to Moderators')
async def report_message(interaction: Interaction, message: Message):
    # We're sending this response message with ephemeral=True, so only the command executor can see it
    await interaction.response.send_message(
        f'Thanks for reporting this message by {message.author.mention} to our moderators.', ephemeral=True
    )

    # Handle report by sending it into a log channel
    log_channel = interaction.guild.get_channel(0)  # replace with your channel id

    embed = Embed(title='Reported Message')
    if message.content:
        embed.description = message.content

    embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    embed.timestamp = message.created_at

    url_view = ui.View()
    url_view.add_item(ui.Button(label='Go to Message', style=ButtonStyle.url, url=message.jump_url))

    await log_channel.send(embed=embed, view=url_view)



def main(client):
    ### Set up logging ###
    logging.basicConfig(level="INFO")
    #load all cogs
    #	for filename in os.listdir("src/cogs"):
    #		if filename.endswith(".py"):
    #			try:
    #				client.load_extension(f"cogs.{filename[:-3]}")
    #				logger.info(f"Loaded cog: {filename[:-3]}")
    #			except Exception as e:
    #				logger.error(f"Failed to load cog: {filename[:-3]}")
    #				logger.error(e)

    #### Run the bot ####
    client.run('token')


### Install runguard
### This is the entry point of the program. It will only run if this file is the one being run.
if __name__ == "__main__":
	main(client=client)