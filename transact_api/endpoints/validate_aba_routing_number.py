from dataclasses import dataclass

from transact_api.endpoints import BaseRequest, BaseResponse


class ValidateAbaRoutingNumberRequest(BaseRequest):
    routingNumber: str


@dataclass
class ValidateAbaRoutingNumberResponse(BaseResponse):
    accountDetails: str
