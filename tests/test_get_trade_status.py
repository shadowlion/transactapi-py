import pytest
import requests
import responses

from transact_api import TransactApiClient
from transact_api.endpoints.get_trade_status import GetTradeStatusResponse

match_request = {
    "clientID": "someclientid",
    "developerAPIKey": "somedeveloperkey",
    "tradeId": "141103099",
}

successful_response = {
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
            "orderId": "141103099",
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
def mocked_responses() -> responses.RequestsMock:
    with responses.RequestsMock() as rsps:
        rsps.add(
            "POST",
            "https://api.norcapsecurities.com/tapiv3/index.php/v3/getTradeStatus",
            status=200,
            content_type="application/json",
            match=[responses.matchers.json_params_matcher(match_request)],
            json=successful_response,
        )
        yield rsps


def test_api_directly(mocked_responses: responses.RequestsMock) -> None:
    resp = requests.request(
        "POST",
        "https://api.norcapsecurities.com/tapiv3/index.php/v3/getTradeStatus",
        json={
            "clientID": "someclientid",
            "developerAPIKey": "somedeveloperkey",
            "tradeId": "141103099",
        },
    )
    assert resp.status_code == 200
    assert resp.json()["statusCode"] == "101"
    assert resp.json()["statusDesc"] == "Ok"
    assert resp.json()["tradeDetails"][0]["orderId"] == "141103099"


def test_api_from_client(mocked_responses: responses.RequestsMock) -> None:
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.get_trade_status(
        trade_id="141103099",
    )
    assert isinstance(res, GetTradeStatusResponse)
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    assert res.trade_details[0].order_id == "141103099"
