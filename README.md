# TransactAPI Python Wrapper

TransactAPI is a RESTful API that enables broker-dealers, funding platforms, and issuers to conduct online private securities offerings. Our standards-based API toolkit can be quickly and easily integrated with proprietary platforms, saving development time and money. Issuers, intermediaries, and advisors can benefit from TransactAPI’s straight-through processing of private placement transactions, which enables higher transaction volumes, expands access to investors, and reduces processing times.

This is a python api wrapper that functions for endpoints as specified in the [documentation](transactapi-docs) of Transact API, provided by [North Capital Private Securities](ncps) (NCPS).

## Author's Notes

This is in no way an official SDK provided by the company itself. However, since I use a lot of python in my daily work life, I figured I could create a library and share it with others in a more open-source format.

For those who wish to help during Hacktoberfest (or any time else!), please submit a PR. Check the [contribution section](#how-to-contribute) for more information.

## Usage

You will need to acquire both a `clientID` and `developerAPIKey` from NCPS - this happens when you subscribe to them as a customer of their services.

Each API endpoint will require both in order to get the response to fully work.

## Development

However, you DO NOT need a `clientID` nor `developerAPIKey` from NCPS, as we use mocks to test each endpoint.

## Installation

```bash
pip install transactapi-py
pipenv install transactapi-py
poetry add transactapi-py
```

## Usage

```python
from transact_api import TransactApiClient
client = TransactApiClient(client_id="", developer_api_key="")
trade = client.get_trade(
    account_id="",
    trade_id="",
)
print(trade.partyDetails[0]["orderId"])
```

## How to Contribute

Take a look at the [documentation](transactapi-docs), find which endpoint hasn't been covered yet. Normally, you will want to do the following on github:

1. Open an issue

2. Open a pull request addressing the issue

3. Set the particular `ENDPOINT` to snake-case. Create the following files:

   - `./transact_api/endpoints/{ENDPOINT}.py` - endpoint file to house dataclasses and typeddicts
   - `./transact_api/__init__.py` - client file to add function + documentation to class
   - `./tests/test_{ENDPOINT}_endpoint.py` - endpoint test file

4. Once all the lints/tests pass locally, edit `pyproject.toml` and bump the version number (e.g. 0.0.1 -> 0.0.2).

5. Await the PR to be approved!

[ncps]: https://www.northcapital.com/
[transactapi-docs]: https://api.norcapsecurities.com/documentation
