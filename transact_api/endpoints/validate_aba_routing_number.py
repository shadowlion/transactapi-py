from dataclasses import dataclass
from typing import Optional, TypedDict


class ValidateAbaRoutingNumberRequest(TypedDict):
    clientID: str
    developerAPIKey: str
    routingNumber: str


@dataclass
class ValidateAbaRoutingNumberResponse:
    statusCode: str
    statusDesc: str
    accountDetails: Optional[str] = None
