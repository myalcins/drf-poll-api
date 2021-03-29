# drf-poll-api


### API Settings
- rename /drf-poll-api/.env.example to .env
- edit .env:
  - ```
    SECRET_KEY=foo
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=db_name
    SQL_USER=user
    SQL_PASSWORD=pass
    SQL_HOST=host
    SQL_PORT=port
    DATABASE=postgres
    ```

### Docker
* Get Docker [Doc](https://docs.docker.com/get-docker/)
* cd /drf-poll-api

```console
$ docker-compose build
$ docker-compose up
```
* open another terminal

```console
$ docker ps
```
* get container id which is the web image

```console
$ sudo docker exec -it <container_id> /bin/bash
root@<container_id>:/# python3 manage.py makemigrations
root@<container_id>:/# python3 manage.py migrate
```

### Note
* If you have a db error like "db_name does not exist"

```console
$ sudo docker exec -it <container_id> /bin/bash
root@<container_id>:/# psql -U <username>
<username>=# create database db_name;
```
