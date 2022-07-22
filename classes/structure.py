from dataclasses import dataclass
from logging import getLogger

from discord import Colour, Embed, PartialEmoji

log = getLogger(__name__)


class CustomEmbed(Embed):
    def __init__(self, *args, **kwargs):
        if "colour" not in kwargs:
            kwargs["colour"] = Colour(0x1E90FF)
        super().__init__(*args, **kwargs)


@dataclass(kw_only=True)
class Links:
    label: str
    url: str = None
    emoji: PartialEmoji.from_str = None
    disabled: bool = False
    custom_id: str = None
    row: int = None


@dataclass(kw_only=True)
class Topic:
    label: str
    id: float
    description: str = None
    content: str
    emoji: PartialEmoji.from_str = None
    image: str = None
    colour: Colour.from_str = 0x1E90FF
    links: list[Links] = None


@dataclass
class Options:  # Category
    options: list[Topic]


@dataclass(kw_only=True)
class CustomBot:
    bot_name: str
    bot_id: int
    owner_name: str
    owner_id: int
    pm2_name: str
    status: bool
