import pytest

from transact_api import TransactApiClient
from transact_api.endpoints.validate_aba_routing_number import (
    ValidateAbaRoutingNumberResponse,
)

example_data_successful = {
    "statusCode": "101",
    "statusDesc": "Ok",
    "accountDetails": "Valid routing number",
}


@pytest.fixture
def mocked_response(mocker):
    example_response = ValidateAbaRoutingNumberResponse(**example_data_successful)
    mocker.patch(
        "transact_api.TransactApiClient.validate_aba_routing_number",
        return_value=example_response,
    )


def test_validate_aba_routing_number(mocked_response):
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.validate_aba_routing_number(
        routing_number="021000012",
    )
    assert isinstance(res, ValidateAbaRoutingNumberResponse)
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    assert res.account_details == "Valid routing number"
