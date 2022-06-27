from dataclasses import dataclass
from datetime import datetime

from transact_api.endpoints import BaseRequest, BaseResponse


class GetTradeStatusRequest(BaseRequest):
    tradeId: str


@dataclass
class TradeDetail:
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

    def __post_init__(self) -> None:
        if type(self.createdDate) is str:
            self.createdDate = datetime.fromisoformat(self.createdDate)


@dataclass
class GetTradeStatusResponse(BaseResponse):
    tradeDetails: TradeDetail