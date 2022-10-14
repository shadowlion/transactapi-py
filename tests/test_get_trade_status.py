import pytest

from transact_api import TransactApiClient
from transact_api.endpoints.get_trade_status import GetTradeStatusResponse

example_data_successful = {
    "statusCode": "101",
    "statusDesc": "Ok",
    "tradeDetails": [
        {
            "id": "787594",
            "developerAPIKey": "somedeveloperkey",
            "offeringId": "someofferingid",
            "accountId": "someaccountid",
            "partyId": "somepartyid",
            "party_type": "",
            "escrowId": None,
            "orderId": "sometradeid",
            "transactionType": "WIRE",
            "totalAmount": "12000.000000",
            "totalShares": "120.000000",
            "orderStatus": "FUNDED",
            "createdDate": "2017-05-17 06:25:38",
            "createdIpAddress": "",
            "errors": "",
            "documentKey": "",
            "esignStatus": "NOTSIGNED",
            "users": "",
            "archived_status": "0",
        }
    ],
}


@pytest.fixture
def mocked_response(mocker):
    example_response = GetTradeStatusResponse(**example_data_successful)
    mocker.patch(
        "transact_api.TransactApiClient.get_trade_status",
        return_value=example_response,
    )


def test_get_trade_status_endpoint(mocked_response):
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.get_trade_status(trade_id="sometradeid")
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    assert len(res.trade_details) == 1
