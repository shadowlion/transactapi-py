from pydantic import BaseModel, Field


class BaseRequest(BaseModel):
    client_id: str
    developer_api_key: str


class BaseResponse(BaseModel):
    status_code: str = Field(alias="statusCode")
    status_desc: str = Field(alias="statusDesc")
