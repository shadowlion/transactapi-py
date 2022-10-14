from transact_api.endpoints import BaseRequest, BaseResponse


class ValidateAbaRoutingNumberRequest(BaseRequest):
    routing_number: str


class ValidateAbaRoutingNumberResponse(BaseResponse):
    account_details: str
