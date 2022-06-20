from dataclasses import dataclass
from typing import List, Optional

from transact_api.endpoints import BaseRequest


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
class GetOfferingResponse:
    statusCode: str
    statusDesc: str
    offeringDetails: Optional[List[OfferingDetail]] = None
