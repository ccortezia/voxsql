import pytest
import textwrap
from voxsql.parser import ParsedFrame, parse
from .cases_parser import CASES as CASES_PARSER


@pytest.mark.parametrize('in_data,expected', CASES_PARSER)
def test_parser(in_data, expected):
    in_data = textwrap.dedent(in_data)
    expected = [ParsedFrame.fromdict(_) for _ in expected]
    parsed = parse(in_data)
    assert len(parsed) == len(expected)
    for parsed_item, expected_item in zip(parsed, expected):
        assert parsed_item.base.header == expected_item.base.header
        assert parsed_item.base.body == expected_item.base.body
        assert parsed_item.base.source == expected_item.base.source
        assert parsed_item.base == expected_item.base
        assert parsed_item.header.source == expected_item.header.source
        assert parsed_item.header.name == expected_item.header.name
        assert parsed_item.header.desc == expected_item.header.desc
        assert parsed_item.header.dialect == expected_item.header.dialect
        for parsed_param_item, expected_param_item in zip(parsed_item.header.params, expected_item.header.params):
            assert parsed_param_item.source == expected_param_item.source
            assert parsed_param_item.name == expected_param_item.name
            assert parsed_param_item.type == expected_param_item.type
            assert parsed_param_item.desc == expected_param_item.desc
        assert parsed_item.header.params == expected_item.header.params
        assert parsed_item.header.retmode == expected_item.header.retmode
        for parsed_retval_item, expected_retval_item in zip(parsed_item.header.retvals, expected_item.header.retvals):
            assert parsed_retval_item.source == expected_retval_item.source
            assert parsed_retval_item.name == expected_retval_item.name
            assert parsed_retval_item.type == expected_retval_item.type
            assert parsed_retval_item.desc == expected_retval_item.desc
        assert parsed_item.header.retvals == expected_item.header.retvals
        assert parsed_item.body.source == expected_item.body.source
        assert parsed_item.body == expected_item.body
        assert parsed_item == expected_item
    assert parsed == expected
