import pytest
import requests
import responses

from transact_api import TransactApiClient
from transact_api.endpoints.get_trade import GetTradeResponse


@pytest.fixture
def mocked_responses() -> responses.RequestsMock:
    with responses.RequestsMock() as rsps:
        rsps.add(
            "POST",
            "https://api.norcapsecurities.com/tapiv3/index.php/v3/getTrade",
            status=200,
            content_type="application/json",
            match=[
                responses.matchers.json_params_matcher(
                    {
                        "clientID": "someclientid",
                        "developerAPIKey": "somedeveloperkey",
                        "accountId": "someaccountid",
                        "tradeId": "sometradeid",
                    }
                ),
            ],
            json={
                "statusCode": "101",
                "statusDesc": "Ok",
                "partyDetails": [
                    {
                        "id": "787508",
                        "developerAPIKey": "somedeveloperkey",
                        "offeringId": "35610",
                        "accountId": "A35513",
                        "partyId": "P82510",
                        "party_type": "IndivACParty",
                        "escrowId": "null",
                        "orderId": "401510522",
                        "transactionType": "WIRE",
                        "totalAmount": "99.400000",
                        "totalShares": "71.000000",
                        "orderStatus": "CREATED",
                        "createdDate": "2014-12-09 04:29:29",
                        "createdIpAddress": "110.172.170.246",
                        "errors": "",
                        "documentKey": "",
                        "esignStatus": "NOTSIGNED",
                        "users": "",
                        "archived_status": "0",
                        "RRApprovalStatus": "Pending",
                        "RRName": "Test",
                        "RRApprovalDate": "09-10-2019",
                        "PrincipalApprovalStatus": "Pending",
                        "PrincipalName": "Test",
                        "PrincipalDate": "09-10-2019",
                    },
                    {
                        "id": "787508",
                        "developerAPIKey": "somedeveloperkey",
                        "offeringId": "35610",
                        "accountId": "A35513",
                        "partyId": "P82510",
                        "party_type": "IndivACParty",
                        "escrowId": "null",
                        "orderId": "401510522",
                        "transactionType": "WIRE",
                        "totalAmount": "99.400000",
                        "totalShares": "71.000000",
                        "orderStatus": "CREATED",
                        "createdDate": "2014-12-09 04:29:29",
                        "createdIpAddress": "110.172.170.246",
                        "errors": "",
                        "documentKey": "",
                        "esignStatus": "NOTSIGNED",
                        "users": "",
                        "archived_status": "0",
                        "RRApprovalStatus": "Pending",
                        "RRName": "Test",
                        "RRApprovalDate": "09-10-2019",
                        "PrincipalApprovalStatus": "Pending",
                        "PrincipalName": "Test",
                        "PrincipalDate": "09-10-2019",
                    },
                    {
                        "id": "787508",
                        "developerAPIKey": "somedeveloperkey",
                        "offeringId": "35610",
                        "accountId": "A35513",
                        "partyId": "P82510",
                        "party_type": "IndivACParty",
                        "escrowId": "null",
                        "orderId": "401510522",
                        "transactionType": "WIRE",
                        "totalAmount": "99.400000",
                        "totalShares": "71.000000",
                        "orderStatus": "CREATED",
                        "createdDate": "2014-12-09 04:29:29",
                        "createdIpAddress": "110.172.170.246",
                        "errors": "",
                        "documentKey": "",
                        "esignStatus": "NOTSIGNED",
                        "users": "",
                        "archived_status": "0",
                        "RRApprovalStatus": "Pending",
                        "RRName": "Test",
                        "RRApprovalDate": "09-10-2019",
                        "PrincipalApprovalStatus": "Pending",
                        "PrincipalName": "Test",
                        "PrincipalDate": "09-10-2019",
                    },
                    {
                        "id": "787508",
                        "developerAPIKey": "somedeveloperkey",
                        "offeringId": "35610",
                        "accountId": "A35513",
                        "partyId": "P82510",
                        "party_type": "IndivACParty",
                        "escrowId": "null",
                        "orderId": "401510522",
                        "transactionType": "WIRE",
                        "totalAmount": "99.400000",
                        "totalShares": "71.000000",
                        "orderStatus": "CREATED",
                        "createdDate": "2014-12-09 04:29:29",
                        "createdIpAddress": "110.172.170.246",
                        "errors": "",
                        "documentKey": "",
                        "esignStatus": "NOTSIGNED",
                        "users": "",
                        "archived_status": "0",
                        "RRApprovalStatus": "Pending",
                        "RRName": "Test",
                        "RRApprovalDate": "09-10-2019",
                        "PrincipalApprovalStatus": "Pending",
                        "PrincipalName": "Test",
                        "PrincipalDate": "09-10-2019",
                    },
                ],
            },
        )

        yield rsps


def test_api_directly(mocked_responses: responses.RequestsMock) -> None:
    resp = requests.request(
        "POST",
        "https://api.norcapsecurities.com/tapiv3/index.php/v3/getTrade",
        json={
            "clientID": "someclientid",
            "developerAPIKey": "somedeveloperkey",
            "accountId": "someaccountid",
            "tradeId": "sometradeid",
        },
    )
    assert resp.status_code == 200
    assert resp.json()["statusCode"] == "101"
    assert resp.json()["statusDesc"] == "Ok"
    assert len(resp.json()["partyDetails"]) == 4


def test_api_from_client(mocked_responses: responses.RequestsMock) -> None:
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.get_trade(
        account_id="someaccountid",
        trade_id="sometradeid",
    )
    assert isinstance(res, GetTradeResponse)
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    assert len(res.party_details) == 4
