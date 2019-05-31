import re


REGEX_FRAME = re.compile(
    r'''\/\*\*\s*?\s*?
    (?P<header>.*?)\*\/\s*
    {(?P<body>.*?)}
    ''', re.S | re.M | re.X
)

REGEX_DESCRIPTION = re.compile(
    r'''(?P<desc>.*?)
    (?=^\s*@|\s*\Z)''',
    re.S | re.M | re.X)

REGEX_NAME = re.compile(
    r'''@name\s+
    (?P<name>.*)
    (?=^\s*@)?''',
    re.X)

REGEX_DIALECT = re.compile(
    r'''@dialect\s+
    (?P<dialect>(sqlite|postgresql|mysql))
    (?=^\s*@)?''',
    re.X)

REGEX_PARAM = re.compile(
    r'''@param\s+
    (?P<name>[a-zA-Z_]+):\s+
    (?P<type>[a-zA-Z\[\]]+)
    (?:\s*-?\s*(?P<desc>.*?))
    (?=^\s*@|\s*\Z)''',
    re.S | re.M | re.X)

REGEX_RETMODE = re.compile(
    r'''@retmode\s+
    (?P<retmode>(scalar|tuples|tuple|records|record))
    (?=^\s*@)?''',
    re.X)

REGEX_RETVAL = re.compile(
    r'''@retval\s+
    (?P<name>[a-zA-Z_]+):\s+
    (?P<type>[a-zA-Z\[\]]+)
    (?:\s*-?\s*(?P<desc>.*?))
    (?=^\s*@|\s*\Z)''',
    re.S | re.M | re.X)
