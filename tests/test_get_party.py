import pytest

from transact_api import TransactApiClient
from transact_api.endpoints.get_party import GetPartyResponse

example_data_successful = {
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
def mocked_response(mocker):
    example_response = GetPartyResponse(**example_data_successful)
    mocker.patch(
        "transact_api.TransactApiClient.get_party",
        return_value=example_response,
    )


def test_get_account(mocked_response):
    party_id = "P79443"
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.get_party(party_id=party_id)
    assert isinstance(res, GetPartyResponse)
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    assert len(res.party_details) == 1
    assert party_id == res.party_details[0].party_id
