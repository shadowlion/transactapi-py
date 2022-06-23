from dataclasses import dataclass
from typing import TypedDict


class BaseRequest(TypedDict):
    clientID: str
    developerAPIKey: str


@dataclass
class BaseResponse:
    statusCode: str
    statusDesc: str
