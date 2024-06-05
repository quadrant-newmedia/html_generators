"""
html_generators - functional html generation

Note - all of our submodules (with the exception)
"""

from ._base import Content
from ._comment import Comment  # noqa
from ._document import Document  # noqa
from ._element import Element, RawTextElement, VoidElement  # noqa
from ._format import format  # noqa
from ._fragment import Fragment  # noqa
from ._join import Join  # noqa
from ._mark_safe import MarkSafe  # noqa
from ._template import template  # noqa
from ._utils import classes, styles  # noqa

# This is for pydoc support, not for "import *" support (which we don't recommend)
__all__ = [
    "Content",
    "Document",
    "Element",
    "Comment",
    "Fragment",
    "format",
    "Join",
    "MarkSafe",
    "template",
    "classes",
    "styles",
    "Html",
    "Body",
    "Head",
    "Title",
    "Address",
    "Article",
    "Aside",
    "Footer",
    "Header",
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "Hgroup",
    "Main",
    "Nav",
    "Section",
    "Blockquote",
    "Dd",
    "Div",
    "Dl",
    "Dt",
    "Figcaption",
    "Figure",
    "Li",
    "Ol",
    "P",
    "Pre",
    "Ul",
    "A",
    "Abbr",
    "B",
    "Bdi",
    "Bdo",
    "Cite",
    "Code",
    "Data",
    "Dfn",
    "Em",
    "I",
    "Kbd",
    "Mark",
    "Q",
    "Rb",
    "Rp",
    "Rt",
    "Rtc",
    "Ruby",
    "S",
    "Samp",
    "Small",
    "Span",
    "Strong",
    "Sub",
    "Sup",
    "Time",
    "U",
    "Var",
    "Audio",
    "Map",
    "Video",
    "Iframe",
    "Object",
    "Picture",
    "Canvas",
    "Noscript",
    "Del",
    "Ins",
    "Caption",
    "Colgroup",
    "Table",
    "Tbody",
    "Td",
    "Tfoot",
    "Th",
    "Thead",
    "Tr",
    "Button",
    "Datalist",
    "Fieldset",
    "Form",
    "Label",
    "Legend",
    "Meter",
    "Optgroup",
    "Option",
    "Output",
    "Progress",
    "Select",
    "Textarea",
    "Details",
    "Dialog",
    "Menu",
    "Summary",
    "Slot",
    "Template",
    "Area",
    "Base",
    "Br",
    "Col",
    "Embed",
    "Hr",
    "Img",
    "Input",
    "Link",
    "Meta",
    "Param",
    "Source",
    "Track",
    "Wbr",
    "Script",
    "Style",
]


## Standard Elements

# List adapted from https://developer.mozilla.org/en-US/docs/Web/HTML/Element June 19, 2020
# (doesn't include svg elements)

# NOTE - we're ignoring some special element types (the template element, escapable raw text elements) and treating them as "normal" -> it makes little to no difference in terms of the html we generate
# escapable raw text elements (ie. <title>) can't have child elements. We _could_ implement those, and do extra validation, but it's not really our job to be an HTML validator - users still have to be aware of which elements are allowed inside which other elements


def Html(*children: Content, **attrs: Content) -> Element:
    return Element("html", *children, **attrs)


def Body(*children: Content, **attrs: Content) -> Element:
    return Element("body", *children, **attrs)


def Head(*children: Content, **attrs: Content) -> Element:
    return Element("head", *children, **attrs)


def Title(*children: Content, **attrs: Content) -> Element:
    return Element("title", *children, **attrs)


def Address(*children: Content, **attrs: Content) -> Element:
    return Element("address", *children, **attrs)


def Article(*children: Content, **attrs: Content) -> Element:
    return Element("article", *children, **attrs)


def Aside(*children: Content, **attrs: Content) -> Element:
    return Element("aside", *children, **attrs)


def Footer(*children: Content, **attrs: Content) -> Element:
    return Element("footer", *children, **attrs)


def Header(*children: Content, **attrs: Content) -> Element:
    return Element("header", *children, **attrs)


def H1(*children: Content, **attrs: Content) -> Element:
    return Element("h1", *children, **attrs)


def H2(*children: Content, **attrs: Content) -> Element:
    return Element("h2", *children, **attrs)


def H3(*children: Content, **attrs: Content) -> Element:
    return Element("h3", *children, **attrs)


def H4(*children: Content, **attrs: Content) -> Element:
    return Element("h4", *children, **attrs)


def H5(*children: Content, **attrs: Content) -> Element:
    return Element("h5", *children, **attrs)


def H6(*children: Content, **attrs: Content) -> Element:
    return Element("h6", *children, **attrs)


def Hgroup(*children: Content, **attrs: Content) -> Element:
    return Element("hgroup", *children, **attrs)


def Main(*children: Content, **attrs: Content) -> Element:
    return Element("main", *children, **attrs)


def Nav(*children: Content, **attrs: Content) -> Element:
    return Element("nav", *children, **attrs)


def Section(*children: Content, **attrs: Content) -> Element:
    return Element("section", *children, **attrs)


def Blockquote(*children: Content, **attrs: Content) -> Element:
    return Element("blockquote", *children, **attrs)


def Dd(*children: Content, **attrs: Content) -> Element:
    return Element("dd", *children, **attrs)


def Div(*children: Content, **attrs: Content) -> Element:
    return Element("div", *children, **attrs)


def Dl(*children: Content, **attrs: Content) -> Element:
    return Element("dl", *children, **attrs)


def Dt(*children: Content, **attrs: Content) -> Element:
    return Element("dt", *children, **attrs)


def Figcaption(*children: Content, **attrs: Content) -> Element:
    return Element("figcaption", *children, **attrs)


def Figure(*children: Content, **attrs: Content) -> Element:
    return Element("figure", *children, **attrs)


def Li(*children: Content, **attrs: Content) -> Element:
    return Element("li", *children, **attrs)


def Ol(*children: Content, **attrs: Content) -> Element:
    return Element("ol", *children, **attrs)


def P(*children: Content, **attrs: Content) -> Element:
    return Element("p", *children, **attrs)


def Pre(*children: Content, **attrs: Content) -> Element:
    return Element("pre", *children, **attrs)


def Ul(*children: Content, **attrs: Content) -> Element:
    return Element("ul", *children, **attrs)


def A(*children: Content, **attrs: Content) -> Element:
    return Element("a", *children, **attrs)


def Abbr(*children: Content, **attrs: Content) -> Element:
    return Element("abbr", *children, **attrs)


def B(*children: Content, **attrs: Content) -> Element:
    return Element("b", *children, **attrs)


def Bdi(*children: Content, **attrs: Content) -> Element:
    return Element("bdi", *children, **attrs)


def Bdo(*children: Content, **attrs: Content) -> Element:
    return Element("bdo", *children, **attrs)


def Cite(*children: Content, **attrs: Content) -> Element:
    return Element("cite", *children, **attrs)


def Code(*children: Content, **attrs: Content) -> Element:
    return Element("code", *children, **attrs)


def Data(*children: Content, **attrs: Content) -> Element:
    return Element("data", *children, **attrs)


def Dfn(*children: Content, **attrs: Content) -> Element:
    return Element("dfn", *children, **attrs)


def Em(*children: Content, **attrs: Content) -> Element:
    return Element("em", *children, **attrs)


def I(*children: Content, **attrs: Content) -> Element:  # noqa: E743
    return Element("i", *children, **attrs)


def Kbd(*children: Content, **attrs: Content) -> Element:
    return Element("kbd", *children, **attrs)


def Mark(*children: Content, **attrs: Content) -> Element:
    return Element("mark", *children, **attrs)


def Q(*children: Content, **attrs: Content) -> Element:
    return Element("q", *children, **attrs)


def Rb(*children: Content, **attrs: Content) -> Element:
    return Element("rb", *children, **attrs)


def Rp(*children: Content, **attrs: Content) -> Element:
    return Element("rp", *children, **attrs)


def Rt(*children: Content, **attrs: Content) -> Element:
    return Element("rt", *children, **attrs)


def Rtc(*children: Content, **attrs: Content) -> Element:
    return Element("rtc", *children, **attrs)


def Ruby(*children: Content, **attrs: Content) -> Element:
    return Element("ruby", *children, **attrs)


def S(*children: Content, **attrs: Content) -> Element:
    return Element("s", *children, **attrs)


def Samp(*children: Content, **attrs: Content) -> Element:
    return Element("samp", *children, **attrs)


def Small(*children: Content, **attrs: Content) -> Element:
    return Element("small", *children, **attrs)


def Span(*children: Content, **attrs: Content) -> Element:
    return Element("span", *children, **attrs)


def Strong(*children: Content, **attrs: Content) -> Element:
    return Element("strong", *children, **attrs)


def Sub(*children: Content, **attrs: Content) -> Element:
    return Element("sub", *children, **attrs)


def Sup(*children: Content, **attrs: Content) -> Element:
    return Element("sup", *children, **attrs)


def Time(*children: Content, **attrs: Content) -> Element:
    return Element("time", *children, **attrs)


def U(*children: Content, **attrs: Content) -> Element:
    return Element("u", *children, **attrs)


def Var(*children: Content, **attrs: Content) -> Element:
    return Element("var", *children, **attrs)


def Audio(*children: Content, **attrs: Content) -> Element:
    return Element("audio", *children, **attrs)


def Map(*children: Content, **attrs: Content) -> Element:
    return Element("map", *children, **attrs)


def Video(*children: Content, **attrs: Content) -> Element:
    return Element("video", *children, **attrs)


def Iframe(*children: Content, **attrs: Content) -> Element:
    return Element("iframe", *children, **attrs)


def Object(*children: Content, **attrs: Content) -> Element:
    return Element("object", *children, **attrs)


def Picture(*children: Content, **attrs: Content) -> Element:
    return Element("picture", *children, **attrs)


def Canvas(*children: Content, **attrs: Content) -> Element:
    return Element("canvas", *children, **attrs)


def Noscript(*children: Content, **attrs: Content) -> Element:
    return Element("noscript", *children, **attrs)


def Del(*children: Content, **attrs: Content) -> Element:
    return Element("del", *children, **attrs)


def Ins(*children: Content, **attrs: Content) -> Element:
    return Element("ins", *children, **attrs)


def Caption(*children: Content, **attrs: Content) -> Element:
    return Element("caption", *children, **attrs)


def Colgroup(*children: Content, **attrs: Content) -> Element:
    return Element("colgroup", *children, **attrs)


def Table(*children: Content, **attrs: Content) -> Element:
    return Element("table", *children, **attrs)


def Tbody(*children: Content, **attrs: Content) -> Element:
    return Element("tbody", *children, **attrs)


def Td(*children: Content, **attrs: Content) -> Element:
    return Element("td", *children, **attrs)


def Tfoot(*children: Content, **attrs: Content) -> Element:
    return Element("tfoot", *children, **attrs)


def Th(*children: Content, **attrs: Content) -> Element:
    return Element("th", *children, **attrs)


def Thead(*children: Content, **attrs: Content) -> Element:
    return Element("thead", *children, **attrs)


def Tr(*children: Content, **attrs: Content) -> Element:
    return Element("tr", *children, **attrs)


def Button(*children: Content, **attrs: Content) -> Element:
    return Element("button", *children, **attrs)


def Datalist(*children: Content, **attrs: Content) -> Element:
    return Element("datalist", *children, **attrs)


def Fieldset(*children: Content, **attrs: Content) -> Element:
    return Element("fieldset", *children, **attrs)


def Form(*children: Content, **attrs: Content) -> Element:
    return Element("form", *children, **attrs)


def Label(*children: Content, **attrs: Content) -> Element:
    return Element("label", *children, **attrs)


def Legend(*children: Content, **attrs: Content) -> Element:
    return Element("legend", *children, **attrs)


def Meter(*children: Content, **attrs: Content) -> Element:
    return Element("meter", *children, **attrs)


def Optgroup(*children: Content, **attrs: Content) -> Element:
    return Element("optgroup", *children, **attrs)


def Option(*children: Content, **attrs: Content) -> Element:
    return Element("option", *children, **attrs)


def Output(*children: Content, **attrs: Content) -> Element:
    return Element("output", *children, **attrs)


def Progress(*children: Content, **attrs: Content) -> Element:
    return Element("progress", *children, **attrs)


def Select(*children: Content, **attrs: Content) -> Element:
    return Element("select", *children, **attrs)


def Textarea(*children: Content, **attrs: Content) -> Element:
    return Element("textarea", *children, **attrs)


def Details(*children: Content, **attrs: Content) -> Element:
    return Element("details", *children, **attrs)


def Dialog(*children: Content, **attrs: Content) -> Element:
    return Element("dialog", *children, **attrs)


def Menu(*children: Content, **attrs: Content) -> Element:
    return Element("menu", *children, **attrs)


def Summary(*children: Content, **attrs: Content) -> Element:
    return Element("summary", *children, **attrs)


def Slot(*children: Content, **attrs: Content) -> Element:
    return Element("slot", *children, **attrs)


def Template(*children: Content, **attrs: Content) -> Element:
    return Element("template", *children, **attrs)


## Void elements: Taken from https://html.spec.whatwg.org/multipage/syntax.html June 19, 2020


def Area(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("area", *children, **attrs)


def Base(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("base", *children, **attrs)


def Br(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("br", *children, **attrs)


def Col(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("col", *children, **attrs)


def Embed(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("embed", *children, **attrs)


def Hr(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("hr", *children, **attrs)


def Img(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("img", *children, **attrs)


def Input(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("input", *children, **attrs)


def Link(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("link", *children, **attrs)


def Meta(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("meta", *children, **attrs)


def Param(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("param", *children, **attrs)


def Source(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("source", *children, **attrs)


def Track(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("track", *children, **attrs)


def Wbr(*children: Content, **attrs: Content) -> VoidElement:
    return VoidElement("wbr", *children, **attrs)


## Raw text elements


def Script(*children: Content, **attrs: Content) -> RawTextElement:
    return RawTextElement("script", *children, **attrs)


def Style(*children: Content, **attrs: Content) -> RawTextElement:
    return RawTextElement("style", *children, **attrs)
