from dataclasses import dataclass
from logging import getLogger
from tkinter import N

from discord import Colour, Embed, PartialEmoji

log = getLogger(__name__)


class CustomEmbed(Embed):
    def __init__(self, *args, **kwargs):
        if "colour" not in kwargs:
            kwargs["colour"] = Colour(0x1E90FF)
        super().__init__(*args, **kwargs)
        self.set_footer(
            text="Thanks for the Icons server for giving us permission to use their lovely icons within our support system",
            icon_url=PartialEmoji.from_str(
                "<:IconsServerCredit:995423046397599764>"
            ).url,
        )


@dataclass(kw_only=True)
class Links:
    label: str
    url: str = None
    emoji: PartialEmoji.from_str = None
    disabled: bool = False
    custom_id: str = None
    row: int = None


@dataclass(kw_only=True)
class Article:
    label: str
    id: float
    description: str = None
    content: str
    image: str = None
    links: list[Links] = None
    emoji: PartialEmoji.from_str = None
    colour: Colour.from_str = 0x1E90FF


@dataclass(kw_only=True)
class Topic:
    label: str
    id: float
    description: str
    content: str
    emoji: PartialEmoji.from_str = None
    colour: Colour = 0x1E90FF
    links: list[Links] = None


@dataclass
class Category:
    articles: list[Topic]


@dataclass
class SubOptions:
    options: list[Article]


@dataclass(kw_only=True)
class CustomBot:
    bot_name: str
    bot_id: int
    owner_name: str
    owner_id: int
    pm2_name: str
    status: bool
