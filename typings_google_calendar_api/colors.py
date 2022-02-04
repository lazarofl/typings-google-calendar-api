import sys
from typing import List, Tuple

from black import Dict

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


class ColorProperties(TypedDict):
    background: str
    foreground: str


class Color(TypedDict):
    kind: str
    updated: str
    calendar: Dict[str, ColorProperties]
    event: Dict[str, ColorProperties]