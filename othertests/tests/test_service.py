import pytest
import othertests as service
import unittest.mock as mock

@mock.patch("othertests.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "mocked oybek"
    user_name = service.get_user_from_db[1]

    assert user_name == "mocked oybek"


    pass