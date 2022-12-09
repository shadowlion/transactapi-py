from typing import List, Union

from pydantic import BaseModel, Field

from transact_api.endpoints import BaseRequest, BaseResponse


class GetPartyRequest(BaseRequest):
    party_id: str

    def as_json(self) -> dict:
        return {
            "clientID": self.client_id,
            "developerAPIKey": self.developer_api_key,
            "partyId": self.party_id,
        }


class PartyDetail(BaseModel):
    party_id: str
    first_name: str
    middle_initial: Union[str, None]
    last_name: str
    domicile: str
    social_security_number: str
    dob: str
    prim_address_1: str
    prim_address_2: Union[str, None]
    prim_city: str
    prim_state: str
    prim_zip: str
    prim_country: str
    email_address: str
    email_address_2: str
    phone: str
    phone_2: str
    occupation: str
    associated_person: str
    emp_country: str
    emp_address_1: str
    emp_address_2: Union[str, None]
    emp_city: str
    emp_state: str
    emp_zip: str
    current_ann_income: str
    avg_ann_income: str
    current_household_income: str
    avg_household_income: str
    household_networth: str
    kyc_status: str
    aml_status: str
    aml_date: str
    tags: str
    notes: str
    field_1: str
    field_2: str
    field_3: str

    class Config:
        @classmethod
        def alias_generator(cls, string: str) -> str:
            init, *the_rest = string.split("_")
            return "".join([init.lower(), *map(str.title, the_rest)])


class GetPartyResponse(BaseResponse):
    party_details: List[PartyDetail] = Field(alias="partyDetails")
