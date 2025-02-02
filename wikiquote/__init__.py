from typing import List, Text

from .quotes import quotes, random_titles, search
from .qotd import quote_of_the_day
from .utils import (
    DisambiguationPageException,
    NoSuchPageException,
    UnsupportedLanguageException,
    MissingQOTDException,
)
from . import langs


def supported_languages() -> List[Text]:
    return sorted(langs.SUPPORTED_LANGUAGES)


qotd = quote_of_the_day


__all__ = [
    "quotes",
    "random_titles",
    "search",
    "qotd",
    "quote_of_the_day",
    "supported_languages",
    "DisambiguationPageException",
    "NoSuchPageException",
    "UnsupportedLanguageException",
    "MissingQOTDException",
]
