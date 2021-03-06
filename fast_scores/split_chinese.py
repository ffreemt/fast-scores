"""Split Chinese by characters and English/numbers by word."""
from typing import List
import re


def insert_spaces(text: str) -> str:
    """Insert space in Chinese characters.

    >>> insert_spaces("test亨利it四世上")
    ' test 亨 利 it 四 世 上 '
    >>> insert_spaces("test亨利it四世上").strip().__len__()
    17
    """
    return re.sub(r"(?<=[a-zA-Z\d]) (?=[a-zA-Z\d])", "", text.replace("", " "))


def split_chinese(text: str, sep=None) -> List[str]:
    """Split Chinese and English."""
    return insert_spaces(text).split()
