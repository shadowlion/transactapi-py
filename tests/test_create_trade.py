import pytest
import requests
import responses

from transact_api import TransactApiClient
from transact_api.endpoints.create_trade import CreateTradeResponse, TransactionType


@pytest.fixture
def mocked_responses() -> responses.RequestsMock:
    with responses.RequestsMock() as rsps:
        rsps.add(
            "POST",
            "https://api.norcapsecurities.com/tapiv3/index.php/v3/createTrade",
            status=200,
            content_type="application/json",
            match=[
                responses.matchers.json_params_matcher(
                    {
                        "clientID": "someclientid",
                        "developerAPIKey": "somedeveloperkey",
                        "accountId": "A12345",
                        "offeringId": "55591",
                        "transactionType": "ACH",
                        "transactionUnits": 200.0,
                    }
                ),
            ],
            json={
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
            },
        )

        yield rsps


def test_api_directly(mocked_responses: responses.RequestsMock) -> None:
    resp = requests.request(
        "POST",
        "https://api.norcapsecurities.com/tapiv3/index.php/v3/createTrade",
        json={
            "clientID": "someclientid",
            "developerAPIKey": "somedeveloperkey",
            "accountId": "A12345",
            "offeringId": "55591",
            "transactionType": "ACH",
            "transactionUnits": 200.0,
        },
    )
    assert resp.status_code == 200
    assert resp.json()["statusCode"] == "101"
    assert resp.json()["statusDesc"] == "Ok"


def test_api_from_client(mocked_responses: responses.RequestsMock) -> None:
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.create_trade(
        offering_id="55591",
        account_id="A12345",
        transaction_type=TransactionType.ACH,
        transaction_units=200.0,
    )
    assert isinstance(res, CreateTradeResponse)
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    assert len(res.purchase_details) == 2
    assert res.purchase_details[0] is True
    # assert isinstance(res.purchase_details[1], PurchaseDetail)
