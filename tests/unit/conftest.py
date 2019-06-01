import os
import pytest

HERE = os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def sample_data_filepath():
    return os.path.join(HERE, 'sample_data.sql')


@pytest.fixture(scope='session')
def sample_data_content():
    with open(os.path.join(HERE, 'sample_data.sql')) as fp:
        return fp.read()
