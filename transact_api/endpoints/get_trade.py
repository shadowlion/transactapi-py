from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Union

from transact_api.endpoints import BaseRequest


class GetTradeRequest(BaseRequest):
    accountId: str
    tradeId: str


@dataclass
class PartyDetail:
    id: int
    developerAPIKey: str
    offeringId: int
    accountId: str
    partyId: str
    partytype: str
    escrowId: str
    orderId: int
    transactionType: str
    totalAmount: str
    totalShares: str
    orderStatus: str
    createdDate: Union[str, datetime]
    createdIpAddress: str
    errors: str
    documentKey: str
    esignStatus: str
    users: str
    archivedstatus: int
    RRApprovalStatus: str
    RRName: str
    RRApprovalDate: str
    PrincipalApprovalStatus: str
    PrincipalName: str
    PrincipalDate: str

    def __post_init__(self) -> None:
        if type(self.createdDate) is str:
            self.createdDate = datetime.fromisoformat(self.createdDate)


@dataclass
class GetTradeResponse:
    statusCode: str
    statusDesc: str
    partyDetails: Optional[List[PartyDetail]] = None
