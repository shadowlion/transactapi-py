from __future__ import annotations

from pydantic import BaseModel

from transact_api.endpoints import BaseRequest, BaseResponse


class GetPartyRequest(BaseRequest):
    party_id: str


class PartyDetail(BaseModel):
    party_id: str
    first_name: str
    middle_initial: str | None
    last_name: str
    domicile: str
    social_security_number: str
    dob: str
    prim_address_1: str
    prim_address_2: str | None
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
    emp_address_2: str | None
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
    party_details: list[PartyDetail]
