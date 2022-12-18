# pull and run Vault with default config
docker run --cap-add=IPC_LOCK -e 'VAULT_LOCAL_CONFIG={"storage": {"file": {"path": "/vault/file"}}, "listener": [{"tcp": { "address": "0.0.0.0:8200", "tls_disable": true}}], "default_lease_ttl": "168h", "max_lease_ttl": "720h", "ui": true}' -p 8200:8200 vault server

curl \
    --header "X-Vault-Token: $VAULT_TOKEN" \
    --request LIST \
    http://127.0.0.1:8200/v1/identity/entity/id