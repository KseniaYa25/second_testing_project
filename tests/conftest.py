import pytest
import requests

from tests.tools_for_tests import get_ids

from tests.configuration import SERVICE_URL

@pytest.fixture(scope="function")
def several_ids():
    ids = get_ids()
    yield ids