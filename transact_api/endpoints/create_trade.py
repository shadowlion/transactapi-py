# from datetime import datetime
from enum import Enum
from typing import List, Union

from pydantic import BaseModel, Field

from transact_api.endpoints import BaseRequest, BaseResponse


class TransactionType(str, Enum):
    ACH = "ACH"
    CHECK = "CHECK"
    WIRE = "WIRE"
    CREDIT_CARD = "CREDITCARD"


class CreateTradeRequest(BaseRequest):
    offering_id: str
    account_id: str
    transaction_type: TransactionType
    transaction_units: float

    def as_json(self) -> dict:
        return {
            "clientID": self.client_id,
            "developerAPIKey": self.developer_api_key,
            "offeringId": self.offering_id,
            "accountId": self.account_id,
            "transactionType": self.transaction_type,
            "transactionUnits": self.transaction_units,
        }


class PurchaseDetail(BaseModel):
    trade_id: int
    transaction_id: str
    transaction_amount: str
    transaction_date: str  # TODO: convert to datetime
    transaction_status: str
    rr_approval_status: str = Field(alias="RRApprovalStatus")
    rr_name: str = Field(alias="RRName")
    rr_approval_date: str = Field(alias="RRApprovalDate")
    principal_approval_status: str = Field(alias="PrincipalApprovalStatus")
    principal_name: str = Field(alias="PrincipalName")
    principal_date: str = Field(alias="PrincipalDate")

    class Config:
        @classmethod
        def alias_generator(cls, string: str) -> str:
            init, *the_rest = string.split("_")
            return "".join([init.lower(), *map(str.title, the_rest)])


class CreateTradeResponse(BaseResponse):
    purchase_details: List[Union[List[PurchaseDetail], bool]] = Field(
        alias="purchaseDetails"
    )
