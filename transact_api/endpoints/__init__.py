from dataclasses import dataclass


@dataclass
class BaseRequest:
    clientID: str
    developerAPIKey: str


@dataclass
class BaseResponse:
    statusCode: str
    statusDesc: str
