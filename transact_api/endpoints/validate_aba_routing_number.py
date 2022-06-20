from dataclasses import dataclass
from typing import Optional

from transact_api.endpoints import BaseRequest


class ValidateAbaRoutingNumberRequest(BaseRequest):
    routingNumber: str


@dataclass
class ValidateAbaRoutingNumberResponse:
    statusCode: str
    statusDesc: str
    accountDetails: Optional[str] = None
