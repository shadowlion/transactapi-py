import pytest
import requests
import responses

from transact_api import TransactApiClient
from transact_api.endpoints.get_offering import GetOfferingResponse

match_request = {
    "clientID": "someclientid",
    "developerAPIKey": "somedeveloperkey",
    "offeringId": "59249",
}

successful_response = {
    "statusCode": "101",
    "statusDesc": "Ok",
    "offeringDetails": [
        {
            "issuerId": "96763",
            "offeringId": "59249",
            "issueName": "NC Offer",
            "issueType": "debt",
            "targetAmount": "20000.000000",
            "minAmount": "100.000000",
            "maxAmount": "25000.000000",
            "unitPrice": "10.000000",
            "totalShares": "2500.000000",
            "remainingShares": "2500.000000",
            "startDate": "10-17-2016",
            "endDate": "12-31-2016",
            "offeringStatus": "Pending",
            "offeringText": "Test",
            "stampingText": None,
        },
    ],
}


@pytest.fixture
def mocked_responses() -> responses.RequestsMock:
    with responses.RequestsMock() as rsps:
        rsps.add(
            "POST",
            "https://api.norcapsecurities.com/tapiv3/index.php/v3/getOffering",
            status=200,
            content_type="application/json",
            match=[responses.matchers.json_params_matcher(match_request)],
            json=successful_response,
        )

        yield rsps


def test_api_directly(mocked_responses: responses.RequestsMock) -> None:
    resp = requests.request(
        "POST",
        "https://api.norcapsecurities.com/tapiv3/index.php/v3/getOffering",
        json={
            "clientID": "someclientid",
            "developerAPIKey": "somedeveloperkey",
            "offeringId": "59249",
        },
    )
    assert resp.status_code == 200
    assert resp.json()["statusCode"] == "101"
    assert resp.json()["statusDesc"] == "Ok"
    assert resp.json()["offeringDetails"][0]["offeringId"] == "59249"


def test_api_from_client(mocked_responses: responses.RequestsMock) -> None:
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.get_offering(
        offering_id="59249",
    )
    assert isinstance(res, GetOfferingResponse)
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    assert res.offering_details[0].offering_id == "59249"
