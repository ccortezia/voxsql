from dataclasses import dataclass
from typing import List
from .framer import read_frames, BaseFrame
from .utils import text_block, text_field

from .regexes import (
    REGEX_DESCRIPTION,
    REGEX_NAME,
    REGEX_DIALECT,
    REGEX_PARAM,
    REGEX_RETMODE,
    REGEX_RETVAL,
)

__all__ = ['parse']


# --------------------------------------------------------------------------------------------------
# Public Symbols
# --------------------------------------------------------------------------------------------------

def parse(text):
    return [
        ParsedFrame.fromdict({
            'base': {
                'source': frame.source,
                'header': frame.header,
                'body': frame.body,
            },
            **_parse_frame(frame)
        })
        for frame in read_frames(text)
    ]


# --------------------------------------------------------------------------------------------------
# Local Private Functions
# --------------------------------------------------------------------------------------------------

def _parse_frame(frame):
    return dict(
        header=_parse_header(frame.header),
        body=_parse_body(frame.body),
    )


def _parse_header(header_text):
    return dict(
        source=header_text,
        name=_parse_header_name(header_text),
        desc=_parse_header_description(header_text),
        dialect=_parse_header_dialect(header_text),
        params=_parse_header_params(header_text),
        retmode=_parse_header_retmode(header_text),
        retvals=_parse_header_retval(header_text),
    )


def _parse_header_description(header_text):
    match = REGEX_DESCRIPTION.match(header_text)
    return match and text_block(match.groups()[0])


def _parse_header_name(header_text):
    match = REGEX_NAME.search(header_text)
    return match and text_field(match.groups()[0])


def _parse_header_dialect(header_text):
    match = REGEX_DIALECT.search(header_text)
    return match and text_field(match.groups()[0])


def _parse_header_params(header_text):
    return [
        {
            'source': text_block(match.group()),
            'name': text_field(match.groupdict()['name']),
            'type': text_field(match.groupdict()['type']),
            'desc': text_block(match.groupdict()['desc']),
        }
        for match in REGEX_PARAM.finditer(header_text)
    ]


def _parse_header_retmode(header_text):
    match = REGEX_RETMODE.search(header_text)
    return match and text_field(match.groups()[0])


def _parse_header_retval(header_text):
    return [
        {
            'source': text_block(match.group()),
            'name': text_field(match.groupdict()['name']),
            'type': text_field(match.groupdict()['type']),
            'desc': text_block(match.groupdict()['desc']),
        }
        for match in REGEX_RETVAL.finditer(header_text)
    ]


def _parse_body(body_text):
    return {'source': text_block(body_text)}


# --------------------------------------------------------------------------------------------------
# Local Data Structures
# --------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class ParsedFrame:
    base: 'BaseFrame'
    header: 'ParsedHeader'
    body: 'ParsedBody'

    @classmethod
    def fromdict(self, data):
        return ParsedFrame(
            base=BaseFrame(**data['base']),
            header=ParsedHeader.fromdict(data['header']),
            body=ParsedBody(**data['body']),
        )


@dataclass(frozen=True)
class ParsedParam:
    source: str
    name: str
    type: str
    desc: str


@dataclass(frozen=True)
class ParsedRetval:
    source: str
    name: str
    type: str
    desc: str


@dataclass(frozen=True)
class ParsedHeader:
    source: str
    name: str
    desc: str
    dialect: str
    params: List[ParsedParam]
    retmode: str
    retvals: List[ParsedRetval]

    @classmethod
    def fromdict(self, data):
        return ParsedHeader(
            source=data["source"],
            name=data["name"],
            desc=data["desc"],
            dialect=data["dialect"],
            params=[ParsedParam(**_) for _ in data["params"]],
            retmode=data["retmode"],
            retvals=[ParsedRetval(**_) for _ in data["retvals"]],
        )


@dataclass(frozen=True)
class ParsedBody:
    source: str
