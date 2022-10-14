from pydantic import BaseModel, Field


class BaseRequest(BaseModel):
    clientID: str = Field(alias="client_id")
    developerAPIKey: str = Field(alias="developer_api_key")


class BaseResponse(BaseModel):
    status_code: str
    status_desc: str

    class Config:
        @classmethod
        def alias_generator(cls, string: str) -> str:
            init, *the_rest = string.split("_")
            return "".join([init.lower(), *map(str.title, the_rest)])
