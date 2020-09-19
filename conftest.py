import pytest


@pytest.fixture(scope='session')
def app():
    return 'app'
