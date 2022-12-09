from pydantic import BaseModel, Field

from transact_api.endpoints import BaseRequest, BaseResponse


class GetAccountRequest(BaseRequest):
    account_id: str

    def as_json(self) -> dict:
        return {
            "clientID": self.client_id,
            "developerAPIKey": self.developer_api_key,
            "accountId": self.account_id,
        }


class AccountDetail(BaseModel):
    account_id: str
    account_name: str
    type: str
    entity_type: str
    resident_type: str
    address_1: str
    address_2: str
    city: str
    state: str
    zip: str
    country: str
    phone: str
    tax_id: str = Field(alias="taxID")
    kyc_status: str
    kyc_date: str
    aml_status: str
    aml_date: str
    suitability_score: str
    suitability_date: str
    suitability_approver: str
    accredited_status: str
    accredited_investor: str
    accredited_investor_date: str
    limit_506c: str = Field(alias="506cLimit")
    account_total_limit: str
    single_investment_limit: str
    associated_ac: str = Field(alias="associatedAC")
    syndicate: str
    tags: str
    notes: str
    approval_status: str
    approval_principal: str
    approval_last_review: str
    field_1: str
    field_2: str
    field_3: str

    class Config:
        @classmethod
        def alias_generator(cls, string: str) -> str:
            init, *the_rest = string.split("_")
            return "".join([init.lower(), *map(str.title, the_rest)])


class GetAccountResponse(BaseResponse):
    account_details: AccountDetail = Field(alias="accountDetails")
