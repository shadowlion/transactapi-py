from typing import TypedDict


class BaseRequest(TypedDict):
    clientID: str
    developerAPIKey: str


class BaseResponse(TypedDict):
    statusCode: str
    statusDesc: str
