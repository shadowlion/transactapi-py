import pytest
from pydantic import ValidationError

from transact_api import TransactApiClient


def test_class_instantiation_no_key():
    with pytest.raises(ValidationError):
        TransactApiClient()


def test_client_instance_with_default_sandbox_behavior():
    client = TransactApiClient(
        client_id="asdf",
        developer_api_key="qwer",
    )
    assert isinstance(client, TransactApiClient)
    assert client.client_id == "asdf"
    assert client.developer_api_key == "qwer"
    assert not client.sandbox


def test_class_instantiation_set_sandbox_to_FALSE():
    client = TransactApiClient(
        client_id="asdf",
        developer_api_key="qwer",
        sandbox=False,
    )
    assert isinstance(client, TransactApiClient)
    assert client.client_id == "asdf"
    assert client.developer_api_key == "qwer"
    assert not client.sandbox


def test_class_instantiation_set_sandbox_to_TRUE():
    client = TransactApiClient(
        client_id="asdf",
        developer_api_key="qwer",
        sandbox=True,
    )
    assert isinstance(client, TransactApiClient)
    assert client.client_id == "asdf"
    assert client.developer_api_key == "qwer"
    assert client.sandbox
