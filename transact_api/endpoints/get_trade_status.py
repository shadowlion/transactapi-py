from datetime import datetime
from typing import TypedDict

from transact_api.endpoints import BaseRequest, BaseResponse


class GetTradeStatusRequest(BaseRequest):
    tradeId: str


class TradeDetail(TypedDict):
    id: int
    developerAPIKey: str
    offeringId: int
    accountId: str
    partyId: str
    partytype: str
    escrowId: None
    orderId: int
    transactionType: str
    totalAmount: str
    totalShares: str
    orderStatus: str
    createdDate: datetime
    createdIpAddress: str
    errors: str
    documentKey: str
    esignStatus: str
    users: str
    archivedstatus: int


class GetTradeStatusResponse(BaseResponse):
    tradeDetails: TradeDetail
