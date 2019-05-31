import pytest
from voxsql.parser import parse
from .cases_binders import CASES as CASES_BINDER_FACTORY


@pytest.mark.parametrize('case,factory_cls,in_data,expected', CASES_BINDER_FACTORY)
def test_binder_factory(case, factory_cls, in_data, expected):
    factory = factory_cls()
    frame = parse(in_data)[0]
    achieved = factory.create(frame)
    assert achieved == expected
