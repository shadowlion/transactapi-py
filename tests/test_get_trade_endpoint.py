import pytest

from transact_api import TransactApiClient
from transact_api.endpoints.get_trade import GetTradeResponse


@pytest.fixture
def mocked_response(mocker):
    example_response = GetTradeResponse(
        **{
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
        }
    )
    mocker.patch(
        "transact_api.TransactApiClient.get_trade",
        return_value=example_response,
    )


def test_get_offering_endpoint(mocked_response):
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.get_trade(
        account_id="someaccountid",
        trade_id="sometradeid",
    )
    assert res.statusCode == "101"
    assert res.statusDesc == "Ok"
    assert len(res.partyDetails) == 4
