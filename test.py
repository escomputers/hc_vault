import json
import os
import requests
import certifi
from dotenv import load_dotenv

# os.environ['SSL_CERT_FILE'] = certifi.where()
VAULT_TOKEN = os.getenv("VAULT_TOKEN")

headers = {"X-Vault-Token": VAULT_TOKEN}
# url = 'http://127.0.0.1:8200/v1/identity/entity/id?list=true'
url = 'http://127.0.0.1:8200/v1/identity/entity/name?list=true'
r = requests.get(url, headers=headers)

response = json.loads(r.text)
res = response['data']['keys']
cleaned_res = ", ".join(res)

# connect to db
# check if result exists in db
# if exists increment counter
# else save to db and start counter