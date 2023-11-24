# 4skl's blog

## Deploy

```sh
docker-compose up web --build -d
```  
or
```sh
docker-compose up web -d
```

## Export db to volume

```sh
docker-compose run --rm db_save
```

## Load db from volume

```sh
docker-compose run --rm db_load
```

## Utils

```sh
docker ps

docker cp <container_id>:/data/ ./4skl_blog/db

docker cp <container_id>:/var/log/ ./4skl_blog/logs

scp -r 4skl.com:./4skl_blog/ ./
```

## TODO

- [ ] Create django models, urls, serializers and views
- [ ] Create frontend using backend api
- [ ] Setup CI with github actions
- [ ] Setup admin user + create fixture with data
- [ ] Deploy to github and add CNAME record to 4skl.com