from dataclasses import dataclass

from transact_api.endpoints import BaseRequest, BaseResponse


@dataclass
class GetOfferingRequest(BaseRequest):
    offeringId: str


@dataclass
class OfferingDetail:
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


@dataclass
class GetOfferingResponse(BaseResponse):
    offeringDetails: OfferingDetail
