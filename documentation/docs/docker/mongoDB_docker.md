## Mongo on Docker

[Mongo Docker Image](https://hub.docker.com/r/library/mongo/)

```bash
$ docker pull mongo

$ docker run --name some-mongo -d mongo
```

This image includes EXPOSE 27017 (the mongo port), so standard container linking will make it automatically available to the linked containers.

### Connect to Mongo from an application

Note: ``--link`` to be deprecated soon.

```bash
docker run --name some-app --link some-mongo:mongo -d application-that-uses-mongo
```

```bash
$ docker run -it --link some-mongo:mongo --rm mongo sh 
    -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/test"'
```

