import requests
import json
import base64
from pprint import pprint

a=requests.get("https://localhost:26657/kujira/unconfirmed_txs").json()
print(a)
