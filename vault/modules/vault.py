import json
import os
import requests
import certifi
from dotenv import load_dotenv

def get_entities():
    # os.environ['SSL_CERT_FILE'] = certifi.where()
    VAULT_TOKEN = os.getenv("VAULT_TOKEN")
    vault_nodes = []
    entities_list = []
    headers = {"X-Vault-Token": VAULT_TOKEN}
    # url = 'http://127.0.0.1:8200/v1/identity/entity/id?list=true'
    url = 'http://127.0.0.1:8200/v1/identity/entity/name?list=true'
    r = requests.get(url, headers=headers)

    response = json.loads(r.text)
    res = response['data']['keys']
    cleaned_res = ", ".join(res)
    entities_list.append(cleaned_res)
    print(cleaned_res)
    print(len(cleaned_res))
    # per ogni nodo in vault_nodes conteggia entità
    # connect to db
    # update counter per il nodo controllato