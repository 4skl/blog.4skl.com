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