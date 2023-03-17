import requests
import json
import base64
from pprint import pprint

def query_kujira_contract_config(contract_address):
    query = {"config": {}}
    query_msg = base64.b64encode(json.dumps(query).encode("utf-8")).decode("utf-8")
    response = requests.get(
        url=f" http://localhost:1317/cosmwasm/wasm/v1/contract/{contract_address}/smart/{query_msg}").json()[
        "data"]
    return response

query=query_kujira_contract_config("kujira14hj2tavq8fpesdwxxcu44rty3hh90vhujrvcmstl4zr3txmfvw9sl4e867")
pprint(query)
