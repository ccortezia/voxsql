import pytest
from .utils import load_case_modules


CASES = [
    pytest.param(module.SOURCE, module.FRAMES, id=case_name)
    for case_name, module in load_case_modules('tests.unit', 'case_parser_').items()
]
