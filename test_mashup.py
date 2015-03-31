from __future__ import unicode_literals
import pytest
from mashup import key_factory



def test_getKey(an_item):
    legal_fields = ['Address',
                    'Average Score',
                    'Business Name',
                    'High Score',
                    'Total Inspections']
    expected = ['605 Queen Anne Avenue North, Seattle, WA 98109, USA',
                23.25,
                "PESO'S",
                62,
                4]

    for field in enumerate(legal_fields):
        get_key = key_factory(field[1])
        assert(get_key(an_item) == expected[field[0]])


@pytest.fixture(scope='function')
def an_item():
    item = {'bbox': [-122.3582709802915,
                      47.6235388197085,
                      -122.3555730197085,
                      47.62623678029149],
            'geometry': {'coordinates': [-122.356922, 47.6248878], 'type': 'Point'},
            'properties': {'Address': '605 Queen Anne Avenue North, Seattle, WA 98109, USA',
                            'Average Score': 23.25,
                            'Business Name': "PESO'S",
                            'High Score': 62,
                            'Total Inspections': 4}
            }
    return item
