from typing import Optional

from pydantic import BaseModel, Field

from transact_api.endpoints import BaseRequest, BaseResponse


class GetTradeStatusRequest(BaseRequest):
    trade_id: str


class TradeDetail(BaseModel):
    id: int
    developer_api_key: str = Field(alias="developerAPIKey")
    offering_id: str
    account_id: str
    party_id: str
    party_type: str = Field(alias="party_type")
    escrow_id: Optional[str] = None
    order_id: str
    transaction_type: str
    total_amount: str
    total_shares: str
    order_status: str
    created_date: str
    created_ip_address: str
    errors: str
    document_key: str
    esign_status: str
    users: str
    archived_status: int = Field(alias="archived_status")

    class Config:
        @classmethod
        def alias_generator(cls, string: str) -> str:
            init, *the_rest = string.split("_")
            return "".join([init.lower(), *map(str.title, the_rest)])


class GetTradeStatusResponse(BaseResponse):
    trade_details: list[TradeDetail]
