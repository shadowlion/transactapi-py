from transact_api.endpoints import BaseRequest, BaseResponse


class ValidateAbaRoutingNumberRequest(BaseRequest):
    routingNumber: str


class ValidateAbaRoutingNumberResponse(BaseResponse):
    accountDetails: str
