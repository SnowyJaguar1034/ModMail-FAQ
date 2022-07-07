from dataclasses import dataclass

from discord import Colour, PartialEmoji


@dataclass(kw_only=True)
class Article:
    label: str
    id: float
    content: str
    image: str = None
    links: dict[str, str] = None
    emoji: PartialEmoji.from_str = None
    colour: Colour = 0x1E90FF


@dataclass
class SubOptions:
    options: list[Article]


@dataclass(kw_only=True)
class Topic:
    label: str
    id: float
    description: str
    content: str
    emoji: PartialEmoji.from_str = None
    colour: Colour = None
    links: dict[str, str] = None


@dataclass
class Category:
    articles: list[Topic]


@dataclass(kw_only=True)
class Links:
    label: str
    url: str
    emoji: PartialEmoji.from_str = None
