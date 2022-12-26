### whoami
Django web app, with Django Q as multiprocessing task queue for fetching data from a list of Hashicorp Vault nodes/cluster and showing to the browser with bootstrap and adminlte.

### pre-requisites
- Docker
- Vault nodes/cluster
- Python >= 3.9

### getting started
1. If you need some Vault nodes
```
python -m pip install -r dev-requirements.txt
python create_vault_cluster.py
```
This will create N Vault nodes (using Docker official image) with this config:
- Seal type: shamir
- Storage type: file (non HA)
- UI enabled
- TLS disabled
- Docker volume ```/vault/logs```, to use for writing persistent audit logs. By default nothing is written here; the file audit backend must be enabled with a path under this directory.
- Docker volume ```/vault/file```, to use for writing persistent storage data when using the file data storage plugin. By default nothing is written here.

Nodes are nitialized with default secret keyshares and key threshold of 1.

Each Vault will listen at ```http://0.0.0.0:<PORT>```
where ```PORT``` will change based on the Vault node number, starting from 8200.

E.g. If 5 nodes are created, you have:
```
http://localhost:8200
http://localhost:8201
http://localhost:8202
http://localhost:8203
http://localhost:8204
```
Unseal keys and root tokens are within ```vault_data.txt```

NB: Vault nodes must be unsealed

2. Set env variables
```
DJANGO_SECRET_KEY
VAULT TOKEN
```
3. Django init
```
python -m pip install -r prod-requirements.txt
python manage.py migrate
python manage.py createsuperuser
```
4. Create Django "superuser" group and assign user to it

5. Enable Django ORM
```
python manage.py createcachetable django_orm_cache_table

# uncomment in settings.py
"""
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_orm_cache_table',
    }
}
"""
```

6. Run
```
python manage.py runserver
python manage.py qcluster
```

7. Create scheduled job
login to http://127.0.0.1:8000/admin/django_q/schedule/
and set required parameters:
```
Name: <whatever>
Func: modules.vault.get_entities
Schedule Type: <whatever>
Cluster: VaultCrawler

```
