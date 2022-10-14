import pytest

from transact_api import TransactApiClient
from transact_api.endpoints.get_account import GetAccountResponse

example_data_successful = {
    "statusCode": "101",
    "statusDesc": "Ok",
    "accountDetails": {
        "accountId": "A77654",
        "accountName": "john",
        "type": "Individual",
        "entityType": "Revocable Trust",
        "residentType": "domestic account",
        "address1": "First street",
        "address2": "Fourth Avenue",
        "city": "ATLANTA",
        "state": "GA",
        "zip": "43543",
        "country": "USA",
        "phone": "4152323232",
        "taxID": "43543543",
        "kycStatus": "pending",
        "kycDate": "2016-02-23 13:29:30",
        "amlStatus": "pending",
        "amlDate": "2016-02-23 13:29:30",
        "suitabilityScore": "5",
        "suitabilityDate": "2016-02-23 13:29:30",
        "suitabilityApprover": "Smith",
        "accreditedStatus": "pending",
        "accreditedInvestor": "income",
        "accreditedInvestorDate": "02-02-2016",
        "506cLimit": "50000",
        "accountTotalLimit": "1000000",
        "singleInvestmentLimit": "1000",
        "associatedAC": "yes",
        "syndicate": "yes",
        "tags": "real estate",
        "notes": "Offers",
        "approvalStatus": "pending",
        "approvalPrincipal": "Charles",
        "approvalLastReview": "12-02-2016",
        "field1": "Account Field 1",
        "field2": "Account Field 2",
        "field3": "Account Field 3",
    },
}


@pytest.fixture
def mocked_response(mocker):
    example_response = GetAccountResponse(**example_data_successful)
    mocker.patch(
        "transact_api.TransactApiClient.get_account",
        return_value=example_response,
    )


def test_get_account(mocked_response):
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.get_account(
        account_id="someaccountid",
    )
    assert isinstance(res, GetAccountResponse)
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    # assert len(res.party_details) == 4
