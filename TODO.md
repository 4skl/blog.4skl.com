Project queryset as pages viewset style
Test tag project filter endpoint
Test featured project endpoint
Docker slow chown
Test project endpoint (list and detail); list should be paginated ? + links to projects should be only theirs handle ?
Move back to 1 dockerfile for prod and add dev setup in readme with sh scripts (ignored by docker build) (needs to run django on localhost:8000 and add the vuejs dev environment api endpoint to this one ?); the problem is creating and having to setup local envs for each dev... (doing packaged prod env, but not dev one; but using docker for dev env is not a good idea (as it takes times to build and docker don't actualize directly with local files), so...)
What viewsets to paginate
Add multi stage builds to dockerfile
Tag model, foreign key as name ? (more data in foreign key, but less queries to get only the name)
Keep url field in project list serializer ?


## TODO
- [x] Add nginx to the docker-compose stack (devcontainer ? instead of the dev infinite sleep loop and to serve static files)
- [x] Copy and improve stack for production (with nginx, gunicorn, postgresql, etc.) and add different dockerfiles based on the dev environment and compose, just with different settings, configuraions, entrypoints, etc.
- [x] Add a docker-compose for development (with hot reload, etc.)
- [x] Add a docker-compose for production (with nginx, gunicorn, etc.)
- [ ] Add a docker-compose for testing (with pytest, fake https and domain, etc.) ?
- [ ] Add django image resizing (with pillow) ? To improve performance and perhaps caching in nginx ? (Improve LCP and so Performance score)
- [ ] Add robots.txt and Document meta description (Improve SEO score)
- [ ] Add a sitemap.xml (Improve SEO score)
- [ ] Move nginx certificate out of the container (to avoid recreating each time the container is recreated) + move nginx server port to another port to avoid conflicts with the outside nginx (and so the outside nginx can proxy_pass to the inside nginx); but still an open question, it seems better to just avoid making dev updates on prod too frequently...
