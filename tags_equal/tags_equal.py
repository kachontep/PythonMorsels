from itertools import groupby
from operator import itemgetter

TAG_START = "<"

TAG_END = ">"


class Tag:
    def __init__(self, name, attributes):
        self._name = name
        self._attributes = attributes

    def __eq__(self, other_tag):
        return (
            self._name == other_tag._name and self._attributes == other_tag._attributes
        )

    def __str__(self):
        return f"{repr(self)}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({repr(self._name)}, {repr(self._attributes)})"
        )

    @staticmethod
    def _parse_tag_name(tag_content):
        tag_content = tag_content.strip()
        if not tag_content.startswith(TAG_START) or not tag_content.endswith(TAG_END):
            raise ValueError(f"{tag_content} is not valid tag string")
        tag_content = tag_content.lstrip(TAG_START).rstrip(TAG_END)
        try:
            pos = tag_content.index(" ")
        except ValueError:
            pos = len(tag_content)
        name = tag_content[:pos]
        name = name.lower()
        invalids = [c not in "abcdefghijklmnopqrstuvwxyz_" for c in name]
        if any(invalids):
            raise ValueError(f"{name} is not valid html tag")
        return name

    @staticmethod
    def _parse_tag_attrs(tag_content, tag_name):
        QUOTES = ['"', "'"]

        def strip_quote(a_val):
            vals = [
                a_val.strip(quote)
                for quote in QUOTES
                if a_val.startswith(quote) and a_val.endswith(quote)
            ]
            return vals[0] if vals else a_val

        def map_content(a_str):
            a_str = a_str.strip()
            if "=" in a_str:
                name, value = a_str.split("=")
                value = strip_quote(value)
            else:
                name, value = a_str, a_str
            return name, value

        def content_parser(tag_content):
            content_start = 0
            in_content = False
            in_quoted = False
            for pos, c in enumerate(tag_content):
                if c != " ":
                    if in_content:
                        if c in QUOTES:
                            in_quoted = not in_quoted
                        continue
                    in_content = True
                    content_start = pos
                elif c == " ":
                    if not in_content or in_quoted:
                        continue
                    yield tag_content[content_start:pos]
                    in_content = False
            if in_content:
                yield tag_content[content_start:]

        tag_content = (
            tag_content.strip()
            .lower()
            .lstrip(TAG_START)
            .rstrip(TAG_END)
            .lstrip(tag_name)
            .strip()
        )
        return [map_content(s) for s in content_parser(tag_content)]

    @staticmethod
    def parse(tag_content):
        name = Tag._parse_tag_name(tag_content)
        attrs = sorted(Tag._parse_tag_attrs(tag_content, name), key=itemgetter(0))
        attrs = set(
            (k, itemgetter(1)(next(vs))) for k, vs in groupby(attrs, key=itemgetter(0))
        )
        return Tag(name, attrs)


def normalize_tag(tag_content):
    return Tag.parse(tag_content)


def tags_equal(tag1, tag2):
    return normalize_tag(tag1) == normalize_tag(tag2)
