from typing import TypedDict

from transact_api.endpoints import BaseRequest, BaseResponse


class GetOfferingRequest(BaseRequest):
    offeringId: str


class OfferingDetail(TypedDict):
    issuerId: str
    offeringId: str
    issueName: str
    issueType: str
    targetAmount: str
    minAmount: str
    maxAmount: str
    unitPrice: str
    totalShares: str
    remainingShares: str
    startDate: str
    endDate: str
    offeringStatus: str
    offeringText: str


class GetOfferingResponse(BaseResponse):
    offeringDetails: OfferingDetail
