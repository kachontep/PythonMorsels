START_TAG = "<"
END_TAG = ">"


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
        if not tag_content.startswith(START_TAG) or not tag_content.endswith(END_TAG):
            raise ValueError(f"{tag_content} is not valid tag string")
        tag_content = tag_content.lstrip(START_TAG).rstrip(END_TAG)
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
        tag_content = (
            tag_content.strip()
            .lower()
            .lstrip(START_TAG)
            .rstrip(END_TAG)
            .lstrip(tag_name)
            .strip()
        )
        for content in tag_content.split(" "):
            content = content.strip()
            if "=" in content:
                name, value = content.split("=")
            else:
                name, value = content, content
            yield name, value
        # pos = 0
        # try:
        #     while True:
        #         op_pos = tag_content.index("=", pos)
        #         try:
        #             val_pos = tag_content.index(" ", op_pos)
        #         except ValueError:
        #             val_pos = len(tag_content)
        #         name = tag_content[pos:op_pos].strip().lower()
        #         value = tag_content[op_pos + 1 : val_pos].strip()
        #         yield name, value
        #         pos = val_pos + 1
        # except ValueError:
        #     pass

    @staticmethod
    def parse(tag_content):
        from itertools import groupby
        from operator import itemgetter

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
