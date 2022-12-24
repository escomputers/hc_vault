### pre-requisites
- Docker
- Vault

### getting started
1. Get Vault
```
docker run --cap-add=IPC_LOCK -e 'VAULT_LOCAL_CONFIG={"storage": {"file": {"path": "/vault/file"}}, "listener": [{"tcp": { "address": "0.0.0.0:8200", "tls_disable": true}}], "default_lease_ttl": "168h", "max_lease_ttl": "720h", "ui": true}' -p 8200:8200 vault server
```
NB: Vault must be unsealed

2. Set env variables
```
DJANGO_SECRET_KEY
VAULT TOKEN
```
3. Django init
```
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
