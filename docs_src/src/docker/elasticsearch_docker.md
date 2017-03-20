# ElasticSearch on Docker

[ElasticSearch Docker Image]( https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html )

```bash
$ docker pull docker.elastic.co/elasticsearch/elasticsearch:5.2.2
$ docker run -p 9200:9200 -e "http.host=0.0.0.0" 
    -e "transport.host=127.0.0.1" docker.elastic.co/elasticsearch/elasticsearch:5.2.2
```

## Custom Image

See [link]( https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html ) above.


You can pass in additional flags to elasticsearch:

```bash
$ docker run -d my-es-image elasticsearch -Des.node.name="TestNode"
```

The standard image comes with a default set of configuration files for elasticsearch, but if you want to provide your own set of configuration files, you can do so via a volume mounted at ``/usr/share/elasticsearch/config``:

```bash
$ docker run -d -v "$PWD/config":/usr/share/elasticsearch/config my-es-image
```

The standard image is configured with a volume at ``/usr/share/elasticsearch/data`` to hold the persisted index data. Use that path if you would like to keep the data in a mounted volume:

```bash
$ docker run -d -v "$PWD/esdata":/usr/share/elasticsearch/data my-es-image
```

The standard image includes ``EXPOSE 9200 9300`` (default http.port), so standard container linking will make it automatically available to the linked containers.

Persistent storage volumes:

```bash
docker volume create --name esdata
docker run --rm -ti -p 9200:9200 -v esdata:/usr/share/elasticsearch/data my-es-image
```

# Kibana on Docker

[Kibana on Docker Documentation](https://www.elastic.co/guide/en/kibana/current/docker.html)

```bash
docker pull docker.elastic.co/kibana/kibana:5.2.2
```
* Access Kibana via [http://localhost:5601]( http://localhost:5601 )
* Access Sense via [http://localhost:5601/app/sense]( http://localhost:5601/app/sense )


### Use of the older image on hub.docker.com

```bash
$ docker run --link some-elasticsearch:elasticsearch -d kibana --plugins /somewhere/else
```

Create Dockerfile: 

```bash
$ touch Dockerfile
$ vi Dockerfile
```

```docker
FROM kibana:latest
RUN gosu kibana kibana plugin --install elastic/sense/latest
EXPOSE 5601
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["kibana"]
```

Build the "docker-kibana-sense" Docker image from the Dockerfile (in current Directory)

```bash
$ docker build -t docker-kibana-sense .
```

ES image comes with a default set of configuration files for elasticsearch, but if you want to provide your own set of configuration files, you can do so via a volume mounted at ``/usr/share/elasticsearch/config``:

```bash
$ docker run --name myES -d -v /c/Users/john.cd/Desktop/docker-elasticsearch/config:/usr/share/elasticsearch/config -p 9200:9200 -p 9300:9300 elasticsearch

$ docker run --name myK --link myES:elasticsearch  -p 5601:5601 -d docker-kibana-sense
```


Alternatively provide the address of elasticsearch via ``ELASTICSEARCH_URL`` environnement variable

```bash
$ docker run --name myK -e ELASTICSEARCH_URL=http://some-elasticsearch:9200 -p 5601:5601 -d kibana
```