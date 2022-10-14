from typing import List

from pydantic import BaseModel, Field

from transact_api.endpoints import BaseRequest, BaseResponse


class GetTradeRequest(BaseRequest):
    account_id: str
    trade_id: str


class PartyDetail(BaseModel):
    id: int
    developer_api_key: str = Field(alias="developerAPIKey")
    offering_id: int
    account_id: str
    party_id: str
    party_type: str = Field(alias="party_type")
    escrow_id: str
    order_id: int
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
    rr_approval_status: str = Field(alias="RRApprovalStatus")
    rr_name: str = Field(alias="RRName")
    rr_approval_date: str = Field(alias="RRApprovalDate")
    principal_approval_status: str = Field(alias="PrincipalApprovalStatus")
    principal_name: str = Field(alias="PrincipalName")
    prinicpal_date: str = Field(alias="PrincipalDate")

    class Config:
        @classmethod
        def alias_generator(cls, string: str) -> str:
            init, *the_rest = string.split("_")
            return "".join([init.lower(), *map(str.title, the_rest)])


class GetTradeResponse(BaseResponse):
    party_details: List[PartyDetail]
