from typing import List

from pydantic import BaseModel, Field

from transact_api.endpoints import BaseRequest, BaseResponse


class GetOfferingRequest(BaseRequest):
    offering_id: str

    def as_json(self) -> dict:
        return {
            "clientID": self.client_id,
            "developerAPIKey": self.developer_api_key,
            "offeringId": self.offering_id,
        }


class OfferingDetail(BaseModel):
    issuer_id: str
    offering_id: str
    issue_name: str
    issue_type: str
    target_amount: str
    min_amount: str
    max_amount: str
    unit_price: str
    total_shares: str
    remaining_shares: str
    start_date: str
    end_date: str
    offering_status: str
    offering_text: str

    class Config:
        @classmethod
        def alias_generator(cls, string: str) -> str:
            init, *the_rest = string.split("_")
            return "".join([init.lower(), *map(str.title, the_rest)])


class GetOfferingResponse(BaseResponse):
    offering_details: List[OfferingDetail] = Field(alias="offeringDetails")
