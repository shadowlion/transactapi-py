from typing import TypedDict


class BaseRequest(TypedDict):
    clientID: str
    developerAPIKey: str
