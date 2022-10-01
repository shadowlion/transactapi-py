# How to Contribute

Take a look at the [documentation](https://api.norcapsecurities.com/documentation), find which endpoint hasn't been covered yet. Normally, you will want to do the following on github:

1. Open an issue

2. Open a pull request addressing the issue

3. Set the particular `ENDPOINT` to snake-case. Create the following files:

   - `./transact_api/endpoints/{ENDPOINT}.py` - endpoint file to house dataclasses and typeddicts
   - `./transact_api/__init__.py` - client file to add function + documentation to class
   - `./tests/test_{ENDPOINT}_endpoint.py` - endpoint test file

4. Once all the lints/tests pass locally, edit `pyproject.toml` and bump the version number (e.g. 0.0.1 -> 0.0.2).

5. Await the PR to be approved!
