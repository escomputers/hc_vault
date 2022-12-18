import json
import os
import requests
import certifi
from dotenv import load_dotenv

# os.environ['SSL_CERT_FILE'] = certifi.where()

VAULT_TOKEN = os.getenv("VAULT_TOKEN")

headers = {"X-Vault-Token": VAULT_TOKEN}
url = 'http://127.0.0.1:8200/v1/identity/entity/id?list=true'
r = requests.get(url, headers=headers)

dict = json.loads(r.text)
print(dict)
# res = dict['data']['metrics']['state']
#last_state = (res.get('value'))