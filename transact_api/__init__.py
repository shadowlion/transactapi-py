import requests
from pydantic import BaseModel

from transact_api.endpoints.create_trade import (
    CreateTradeRequest,
    CreateTradeResponse,
    TransactionType,
)
from transact_api.endpoints.get_account import GetAccountRequest, GetAccountResponse
from transact_api.endpoints.get_offering import GetOfferingRequest, GetOfferingResponse
from transact_api.endpoints.get_party import GetPartyRequest, GetPartyResponse
from transact_api.endpoints.get_trade import GetTradeRequest, GetTradeResponse
from transact_api.endpoints.get_trade_status import (
    GetTradeStatusRequest,
    GetTradeStatusResponse,
)
from transact_api.endpoints.validate_aba_routing_number import (
    ValidateAbaRoutingNumberRequest,
    ValidateAbaRoutingNumberResponse,
)
from transact_api.errors import ERRORS


class TransactApiClient(BaseModel):
    client_id: str
    developer_api_key: str
    sandbox: bool = False

    @property
    def __base_url(self):
        domain = "api-sandboxdash" if self.sandbox else "api"
        return f"https://{domain}.norcapsecurities.com/tapiv3/index.php/v3"

    def get_offering(self, offering_id: str) -> GetOfferingResponse:
        """
        This method is used to get all the details of an offering.
        The Offering ID is required to get the information.

        Reference: https://transactapi.readme.io/reference/getoffering

        Args:
            offering_id (str) Offering ID that is generated by the API when an
            Offering is created (createOffering).

        Returns:
            (GetOfferingResponse) response object
        """
        payload = GetOfferingRequest(
            client_id=self.client_id,
            developer_api_key=self.developer_api_key,
            offering_id=offering_id,
        ).as_json()
        r = requests.post(self.__base_url + "/getOffering", json=payload)
        assert r.status_code == 200, f"Bad API call: {r.status_code}"
        res = GetOfferingResponse(**r.json())
        assert res.status_code == "101", ERRORS[res.status_code]
        return res

    def get_trade(self, account_id: str, trade_id: str) -> GetTradeResponse:
        """This method is used to get all the details of all the trades for an
        account. The Account ID is required to get the details.

        Reference: https://transactapi.readme.io/reference/gettrade

        Args:
            account_id (str) Account ID generated by the API
            trade_id (str) Trade ID generated by the API

        Returns:
            (GetTradeResponse) response object
        """
        payload = GetTradeRequest(
            client_id=self.client_id,
            developer_api_key=self.developer_api_key,
            account_id=account_id,
            trade_id=trade_id,
        ).as_json()
        r = requests.post(self.__base_url + "/getTrade", json=payload)
        assert r.status_code == 200, f"Bad API call: {r.status_code}"
        res = GetTradeResponse(**r.json())
        assert res.status_code == "101", ERRORS[res.status_code]
        return res

    def validate_aba_routing_number(
        self,
        routing_number: str,
    ) -> ValidateAbaRoutingNumberResponse:
        """This method is used to validate the routing number for an external account
        (createExternalAccount).

        Reference: https://transactapi.readme.io/reference/validateabaroutingnumber

        Args:
            routing_number (str) The routing number to be validated

        Returns:
            (ValidateAbaRoutingNumberResponse) response object
        """

        payload = ValidateAbaRoutingNumberRequest(
            client_id=self.client_id,
            developer_api_key=self.developer_api_key,
            routing_number=routing_number,
        ).as_json()
        r = requests.post(self.__base_url + "/validateABARoutingNumber", json=payload)
        assert r.status_code == 200, f"Bad API call: {r.status_code}"
        res = ValidateAbaRoutingNumberResponse(**r.json())
        assert res.status_code == "101", ERRORS[res.status_code]
        return res

    def get_trade_status(self, trade_id: str) -> GetTradeStatusResponse:
        """This method is used to retrieve the status and all other current
        information for a specific trade. The TradeID is required as a request
        parameter for this method.

        Reference: https://transactapi.readme.io/reference/gettradestatus

        Args:
            trade_id (str) Trade ID generated by the API

        Returns:
            (GetTradeStatusResponse) response object
        """
        payload = GetTradeStatusRequest(
            client_id=self.client_id,
            developer_api_key=self.developer_api_key,
            trade_id=trade_id,
        ).as_json()
        r = requests.post(self.__base_url + "/getTradeStatus", json=payload)
        assert r.status_code == 200, f"Bad API call: {r.status_code}"
        res = GetTradeStatusResponse(**r.json())
        assert res.status_code == "101", ERRORS[res.status_code]
        return res

    def get_account(self, account_id: str) -> GetAccountResponse:
        """This method is used to get all information for an account (createAccount).

        Reference: https://transactapi.readme.io/reference/getaccount

        Args:
            account_id (str) Account ID that is generated by the API once an account is
            created (createAccount).

        Returns:
            (GetAccountResponse) response object
        """
        payload = GetAccountRequest(
            client_id=self.client_id,
            developer_api_key=self.developer_api_key,
            account_id=account_id,
        ).as_json()
        r = requests.post(self.__base_url + "/getAccount", json=payload)
        assert r.status_code == 200, f"Bad API call: {r.status_code}"
        res = GetAccountResponse(**r.json())
        assert res.status_code == "101", ERRORS[res.status_code]
        return res

    def get_party(self, party_id: str) -> GetPartyResponse:
        """This method is used to get all information about an individual Party. The
        Party ID must be specified as a request parameter to get the party information.

        Reference: https://transactapi.readme.io/reference/getparty

        Args:
            party_id (str): Party ID that is generated by the API once an individual
            party is created (createParty)
        """
        payload = GetPartyRequest(
            client_id=self.client_id,
            developer_api_key=self.developer_api_key,
            party_id=party_id,
        ).as_json()
        r = requests.post(self.__base_url + "/getParty", json=payload)
        assert r.ok, f"Bad API call: {r.status_code}"
        res = GetPartyResponse(**r.json())
        assert res.status_code == "101", ERRORS[res.status_code]
        return res

    def create_trade(
        self,
        offering_id: str,
        account_id: str,
        transaction_type: TransactionType,
        transaction_units: float,
    ):
        """This method is used to create a trade/investment for an offering. This
        requires Account ID and the total number of units/shares to be purchased by the
        account. Creating a trade represents the intention to invest and does NOT
        initiate any sort of fund move. To initiate an ACH transfer for a trade, you
        will need to use the externalFundMove method.

        Reference: https://transactapi.readme.io/reference/createtrade

        Args:
            offering_id (str): Offering ID that is generated by the API when an
            offering is created (createOffering)
            account_id (str): Account ID of the account that is investing (this account
            should have one primary party)
            transaction_type (TransactionType): Transaction Type as:
            ACH / WIRE / CHECK/ CREDITCARD / TBD/IRA
            transaction_units (float): Number of units/shares to be purchased
        """
        payload = CreateTradeRequest(
            client_id=self.client_id,
            developer_api_key=self.developer_api_key,
            offering_id=offering_id,
            account_id=account_id,
            transaction_type=transaction_type,
            transaction_units=transaction_units,
        ).as_json()
        r = requests.post(self.__base_url + "/createTrade", json=payload)
        assert r.ok, f"Bad API call: {r.status_code}"
        res = CreateTradeResponse(**r.json())
        assert res.status_code == "101", ERRORS[res.status_code]
        return res
