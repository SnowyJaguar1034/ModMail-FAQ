from logging import getLogger
from typing import Union

from discord import Forbidden, HTTPException, InteractionResponse, Member, Role, User

log = getLogger(__name__)


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
    except HTTPException as e:
        log.error(f"Could not change roles for {user.name} due to an HTTP error.\n{e}")
    await response.send_message(
        f"Successfully {action}ed {role.mention} role for {user}",
        ephemeral=True,
    )
