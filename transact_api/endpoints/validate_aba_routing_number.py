from pydantic import Field

from transact_api.endpoints import BaseRequest, BaseResponse


class ValidateAbaRoutingNumberRequest(BaseRequest):
    routing_number: str

    def as_json(self) -> dict:
        return {
            "clientID": self.client_id,
            "developerAPIKey": self.developer_api_key,
            "routingNumber": self.routing_number,
        }


class ValidateAbaRoutingNumberResponse(BaseResponse):
    account_details: str = Field(alias="accountDetails")
