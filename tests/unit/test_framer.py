import pytest
import textwrap
from voxsql.framer import BaseFrame, read_frames
from .cases_framer import CASES as CASES_FRAMER


@pytest.mark.parametrize('case,text,frames', CASES_FRAMER, ids=lambda x: x[:10])
def test_framer(case, text, frames):
    text = textwrap.dedent(text)
    expected = [BaseFrame(source=text, **frame) for frame in frames]
    achieved = read_frames(text)
    assert len(expected) == len(achieved)
    for idx, (expected_frame, achieved_frame) in enumerate(zip(expected, achieved)):
        assert expected_frame == achieved_frame, f"Frame {idx} does not match expectation"
