import docker
import requests
import time

docker_client = docker.from_env()
port = 8200
for i in range(1,3):
    port += 1
    vault_config = {'VAULT_LOCAL_CONFIG': '{"storage": {"file": {"path": "/vault/file"}}, "listener": [{"tcp": {"address": "0.0.0.0:' + str(port) + '",' + ' "tls_disable": "true"}}], "default_lease_ttl": "168h", "max_lease_ttl": "720h", "ui": "true"}'}

    docker_client.containers.run('vault', name="vault"+ str(i), command='server', environment=vault_config, cap_add=['IPC_LOCK'], ports={str(port)+'/tcp': port}, detach=True)
    VAULT_ADDR = 'http://127.0.0.1:' + str(port)

    url = VAULT_ADDR + '/v1/sys/init'
    ploads = {"secret_shares": 1, "secret_threshold": 1}
    time.sleep(10)
    r = requests.post(url, json = ploads)

    file_content = r.text + r.url + '\n'
    with open('vault_data.txt', 'a') as f:
        f.write(file_content)
        f.close()
