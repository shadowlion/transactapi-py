import pytest

from transact_api import TransactApiClient
from transact_api.endpoints.create_trade import CreateTradeResponse

example_data_successful = {
    "statusCode": "101",
    "statusDesc": "Ok",
    "purchaseDetails": [
        True,
        [
            {
                "tradeId": "130",
                "transactionId": "476693475244",
                "transactionAmount": "2500.55",
                "transactionDate": "2014-12-09 04:29:29",
                "transactionStatus": "CREATED",
                "RRApprovalStatus": "Pending",
                "RRName": "Test",
                "RRApprovalDate": "09-10-2019",
                "PrincipalApprovalStatus": "Pending",
                "PrincipalName": "Test",
                "PrincipalDate": "09-10-2019",
            }
        ],
    ],
}


@pytest.fixture
def mocked_response(mocker):
    example_response = CreateTradeResponse(**example_data_successful)
    mocker.patch(
        "transact_api.TransactApiClient.create_trade",
        return_value=example_response,
    )


def test_get_account(mocked_response):
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.create_trade(
        offering_id="55591",
        account_id="A12345",
        transaction_type="ACH",
        transaction_units=200.0,
    )
    assert isinstance(res, CreateTradeResponse)
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    # assert len(res.party_details) == 4
