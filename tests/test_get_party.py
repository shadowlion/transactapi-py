import pytest
import requests
import responses

from transact_api import TransactApiClient
from transact_api.endpoints.get_party import GetPartyResponse

match_request = {
    "clientID": "someclientid",
    "developerAPIKey": "somedeveloperkey",
    "partyId": "P79443",
}

successful_response = {
    "statusCode": "101",
    "statusDesc": "Ok",
    "partyDetails": [
        {
            "partyId": "P79443",
            "firstName": "John",
            "middleInitial": "D",
            "lastName": "Smith",
            "domicile": "U.S. citizen",
            "socialSecurityNumber": "112-22-3333",
            "dob": "03-24-1972",
            "primAddress1": "PEACHTREE PLACE",
            "primAddress2": "PEACHTREE PLACE",
            "primCity": "Atlanta",
            "primState": "GA",
            "primZip": "30318",
            "primCountry": "USA",
            "emailAddress": "john@gmail.com",
            "emailAddress2": "smith@gmail.com",
            "phone": "9876543210",
            "phone2": "0123456789",
            "occupation": "DEVELOPER",
            "associatedPerson": "Yes",
            "empCountry": "USA",
            "empAddress1": "PEACHTREE PLACE",
            "empAddress2": "PEACHTREE PLACE",
            "empCity": "Atlanta",
            "empState": "GA",
            "empZip": "30318",
            "currentAnnIncome": "200000",
            "avgAnnIncome": "500000",
            "currentHouseholdIncome": "300000",
            "avgHouseholdIncome": "400000",
            "householdNetworth": "200000",
            "kycStatus": "pending",
            "amlStatus": "pending",
            "amlDate": "03-17-2016",
            "tags": "Tags Added",
            "notes": "Notes Added",
            "field1": "Account Field 1",
            "field2": "Account Field 2",
            "field3": "Account Field 3",
        }
    ],
}


@pytest.fixture
def mocked_responses() -> responses.RequestsMock:
    with responses.RequestsMock() as rsps:
        rsps.add(
            "POST",
            "https://api.norcapsecurities.com/tapiv3/index.php/v3/getParty",
            status=200,
            content_type="application/json",
            match=[responses.matchers.json_params_matcher(match_request)],
            json=successful_response,
        )
        yield rsps


def test_api_directly(mocked_responses: responses.RequestsMock) -> None:
    resp = requests.request(
        "POST",
        "https://api.norcapsecurities.com/tapiv3/index.php/v3/getParty",
        json={
            "clientID": "someclientid",
            "developerAPIKey": "somedeveloperkey",
            "partyId": "P79443",
        },
    )
    assert resp.status_code == 200
    assert resp.json()["statusCode"] == "101"
    assert resp.json()["statusDesc"] == "Ok"
    assert resp.json()["partyDetails"][0]["partyId"] == "P79443"


def test_api_from_client(mocked_responses: responses.RequestsMock) -> None:
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.get_party(
        party_id="P79443",
    )
    assert isinstance(res, GetPartyResponse)
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    assert res.party_details[0].party_id == "P79443"
    assert len(res.party_details) == 1
