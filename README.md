# drf-poll-api


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
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

