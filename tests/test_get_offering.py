import pytest

from transact_api import TransactApiClient
from transact_api.endpoints.get_offering import GetOfferingResponse

example_data_successful = {
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
def mocked_response(mocker):
    example_response = GetOfferingResponse(**example_data_successful)
    mocker.patch(
        "transact_api.TransactApiClient.get_offering",
        return_value=example_response,
    )


def test_get_offering_endpoint(mocked_response):
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.get_offering("someofferingid")
    assert isinstance(res, GetOfferingResponse)
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    assert len(res.offering_details) == 1
