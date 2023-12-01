# 4skl's blog  
* For now the `main` branch is considered to be `dev` branch, once it'll be stable enough it'll be considered as the `prod` branch. And a `dev` branch will be created.  

## Deploy

```sh
docker-compose up --build -d
```  
or
```sh
docker-compose up -d
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