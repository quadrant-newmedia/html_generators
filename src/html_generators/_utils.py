"""
Various utility methods for building html attributes.
"""

from typing import Iterable

from ._base import OptionalString


# Note: not sure why this passes type testing and filter(None, optional_strings) doesn't
def _iter_strings(optional_strings: Iterable[OptionalString]) -> Iterable[str]:
    for s in optional_strings:
        if s:
            yield s


def styles(*_styles: OptionalString):
    return "; ".join(_iter_strings(_styles))


def classes(*_classes: OptionalString):
    return " ".join(_iter_strings(_classes))
