from dataclasses import dataclass
from typing import List
from .regexes import REGEX_FRAME
from .utils import text_block


__all__ = ['read_frames']


@dataclass(frozen=True)
class BaseFrame:
    source: str
    header: str
    body: str


def read_frames(text: str) -> List[BaseFrame]:
    """Extracts text frames from the given raw text

    Parameters
    ----------
    text : str
        Text containing voxsql-compliant documented queries

    Returns
    -------
    List of TextFrame
        Frames identified within the given text block
    """
    return [
        BaseFrame(
            source=text_block(text),
            header=text_block(_clean_lborder(match.groupdict()["header"])),
            body=text_block(match.groupdict()["body"])
        )
        for match in REGEX_FRAME.finditer(text)]


def _clean_lborder(text: str, char='*') -> str:
    text_lines = text.splitlines()
    unprefixed_lines = [line.lstrip().lstrip('*') for line in text_lines]
    return '\n'.join(unprefixed_lines)
