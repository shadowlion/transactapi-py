"""Custom Error Codes.

Reference: https://api.norcapsecurities.com/admin_v3/documentation/errorCodeList
"""


class CustomError(Exception):
    pass


class Status102Error(CustomError):
    def __str__(self) -> str:
        return "Bad request"


class Status103Error(CustomError):
    def __str__(self) -> str:
        return "Invalid Developer Key/Client ID"


class Status104Error(CustomError):
    def __str__(self) -> str:
        return "The requested class does not exist"


class Status105Error(CustomError):
    def __str__(self) -> str:
        return "Invalid request"


class Status162Error(CustomError):
    def __str__(self) -> str:
        return "Offering ID/Client ID does not match"


class Status215Error(CustomError):
    def __str__(self) -> str:
        return "Invalid routing number"


ERRORS = {
    "102": Status102Error,
    "103": Status103Error,
    "104": Status104Error,
    "105": Status105Error,
    "162": Status162Error,
    "215": Status215Error,
}
