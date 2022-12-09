import pytest
import requests
import responses

from transact_api import TransactApiClient
from transact_api.endpoints.validate_aba_routing_number import (
    ValidateAbaRoutingNumberResponse,
)


@pytest.fixture
def mocked_responses() -> responses.RequestsMock:
    with responses.RequestsMock() as rsps:
        rsps.add(
            "POST",
            "https://api.norcapsecurities.com/tapiv3/index.php/v3/validateABARoutingNumber",  # noqa E502
            status=200,
            content_type="application/json",
            match=[
                responses.matchers.json_params_matcher(
                    {
                        "clientID": "someclientid",
                        "developerAPIKey": "somedeveloperkey",
                        "routingNumber": "021000012",
                    }
                ),
            ],
            json={
                "statusCode": "101",
                "statusDesc": "Ok",
                "accountDetails": "Valid routing number",
            },
        )

        yield rsps


def test_api_directly(mocked_responses: responses.RequestsMock) -> None:
    resp = requests.request(
        "POST",
        "https://api.norcapsecurities.com/tapiv3/index.php/v3/validateABARoutingNumber",
        json={
            "clientID": "someclientid",
            "developerAPIKey": "somedeveloperkey",
            "routingNumber": "021000012",
        },
    )
    assert resp.status_code == 200
    assert resp.json()["statusCode"] == "101"
    assert resp.json()["statusDesc"] == "Ok"
    assert resp.json()["accountDetails"] == "Valid routing number"


def test_api_from_client(mocked_responses: responses.RequestsMock) -> None:
    client = TransactApiClient(
        client_id="someclientid",
        developer_api_key="somedeveloperkey",
    )
    res = client.validate_aba_routing_number(
        routing_number="021000012",
    )
    assert isinstance(res, ValidateAbaRoutingNumberResponse)
    assert res.status_code == "101"
    assert res.status_desc == "Ok"
    assert res.account_details == "Valid routing number"
