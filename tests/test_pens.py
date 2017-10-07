# Only call from tests/ directory

import vcr
from pytest import fixture
from codepen import Pens

"""
Constants
"""
CATEGORY = 'popular'
PAGE = 2

@fixture
def pen_keys():
    # Responsible only for returning the test data (keys for pens)
    return ['title', 'details', 'link', 'id', 'views', 'loves', 'comments', 'images', 'user']

@vcr.use_cassette('vcr_cassettes/pens.yml')
def test_pens_list(pen_keys):
    """Tests an API call to get a list of pens"""

    response = Pens.list(CATEGORY, PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(pen_keys).issubset(response[0].keys()), "All keys should be in the response"