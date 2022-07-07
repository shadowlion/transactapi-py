import pytest

from transact_api import TransactApiClient


def test_class_instantiation_no_key():
    with pytest.raises(TypeError):
        TransactApiClient()


def test_class_instantiation_with_keys():
    client = TransactApiClient(client_id="asdf", developer_api_key="qwer")
    # assert isinstance(client, TransactApiClient)
    assert client.client_id == "asdf"
    assert client.developer_api_key == "qwer"
    assert not client.sandbox
    # assert client.__base_url == "https://api.norcapsecurities.com/tapiv3/index.php/v3"
