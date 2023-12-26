# 4skl's blog  
* For now the `main` branch is considered to be `dev` branch, once it'll be stable enough it'll be considered as the `prod` branch. And a `dev` branch will be created.  

## Dev setup  

### Requirements

- Docker
- Docker-compose
- VSCode
- VSCode Devcontainer extension
- Other VSCode extensions (see `.devcontainer/devcontainer.json`)  

Just open the project in VSCode and it'll ask you to open it in a devcontainer.

## Deploy

```sh
docker-compose up --build --force-recreate -d
```  
or
```sh
docker-compose up -d
```

## Utils

todo: add more utils
```sh
docker ps

docker cp <prod_container_id>:/var/www/4skl.com/media ./4skl_blog/media

scp -r ...
```

## TODO

- [x] Create django models, urls, serializers and views
- [x] Setup admin user + create fixture with data
- [~] Create frontend using backend REST API
- [x] Checkout devcontainer for dev setup
- [ ] Setup prod env with docker-compose, and prepare for prod + branch to dev once done
- [ ] Deploy to VPS and setup nginx + ssl