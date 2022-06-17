import pytest

from transact_api import TransactApiClient
from transact_api.endpoints.validate_aba_routing_number import (
    ValidateAbaRoutingNumberResponse,
)


@pytest.fixture
def mocked_response(mocker):
    example_response = ValidateAbaRoutingNumberResponse(
        **{
            "statusCode": "101",
            "statusDesc": "Ok",
            "accountDetails": "Valid routing number",
        }
    )
    mocker.patch(
        "transact_api.TransactApiClient.validate_aba_routing_number",
        return_value=example_response,
    )


def test_validate_aba_routing_number_endpoint(mocked_response):
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.validate_aba_routing_number("021000012")
    assert res.statusCode == "101"
    assert res.statusDesc == "Ok"
    assert res.accountDetails == "Valid routing number"
