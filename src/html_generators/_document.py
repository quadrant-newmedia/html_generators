from typing import Iterator

from ._base import Content, HTMLGenerator, generate_html
from ._element import Element


class Document(HTMLGenerator):
    """
    A complete HTML document

    Merely adds the required DOCTYPE line.

    If you specify html_attrs, all children will be wrapped in an <html>
    element with the specified attrs. Just a shortcut.
    """

    def __init__(self, *children: Content, **html_attrs: Content):
        self._children = [Element("html", children, **html_attrs)] if html_attrs else children

    def __iter__(self) -> Iterator[str]:
        yield "<!DOCTYPE html>\n"
        yield from generate_html(self._children)
