from logging import getLogger
from typing import Union

from discord import (
    Forbidden,
    HTTPException,
    Interaction,
    InteractionResponse,
    Member,
    Role,
    User,
)

from topics import aspects, how_to_commands, initial, premium, trouleshooting

log = getLogger(__name__)

# Get the list of initial articles and map them id:label to display correct label title later
mainoptions_mapping = {}
for article in initial.options:
    mainoptions_mapping[article.id] = article.label

# Get the list of sub-questions to display, based on their selection
suboption_mapping = {}
suboptions = [trouleshooting, premium, how_to_commands, aspects]
for suboption in suboptions:
    for article in suboption.options:
        if article.id not in suboption_mapping.keys():
            suboption_mapping[int(article.id)] = suboption


async def further_support(
    action: str, role: Role, user: Union[User, Member], response: InteractionResponse
):
    try:
        if action == "remove":
            await user.remove_roles(
                *[role],
                reason="User no longer needs further support",
            )
        elif action == "add":
            await user.add_roles(
                *[role],
                reason="User requested further support",
            )
    except Forbidden as e:
        log.error(
            f"Could not change roles for {user.name} due to insufficient permissions. (Forbidden):\n{e}"
        )
    except HTTPException:
        log.error(f"Could not change roles for {user.name} due to an HTTP error.\n{e}")
    await response.send_message(
        f"Successfully {action}ed {role.mention} role for {user}",
        ephemeral=True,
    )
