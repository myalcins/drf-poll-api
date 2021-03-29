# drf-poll-api


### API Settings
* change /drf-poll-api/.env.example name to .env
* add SECRET_KEY
* add database settings (look at key of database settings in the production settings file)
* add DATABASE=postgres

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
