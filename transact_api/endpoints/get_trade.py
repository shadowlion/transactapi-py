from typing import List, TypedDict

from transact_api.endpoints import BaseRequest, BaseResponse


class GetTradeRequest(BaseRequest):
    accountId: str
    tradeId: str


class PartyDetail(TypedDict):
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
    createdDate: str
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


class GetTradeResponse(BaseResponse):
    partyDetails: List[PartyDetail]
