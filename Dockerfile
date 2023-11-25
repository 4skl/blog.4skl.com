FROM alpine:latest as base

RUN apk add --update

RUN mkdir -p /var/www/4skl/

# Build vue app
# Create the folder for the built frontend
WORKDIR /var/www/4skl/
# Move into the frontend folder and create it
WORKDIR /usr/src/app/frontend/
RUN apk add --update npm
COPY ./4skl .
RUN npm i
RUN npm run build
RUN cp -r dist/ /var/www/4skl/
# Move out of the frontend folder to delete it
WORKDIR /
RUN rm -r /usr/src/app/frontend/



# Reverse proxy setup
RUN apk add --no-cache nginx
RUN mkdir -p /var/log/nginx/
RUN chown -R nginx /var/www/4skl /var/lib/nginx/ /var/log/nginx/
WORKDIR /etc/nginx/http.d/
COPY default.conf default.conf


# Backend setup

# Create a new user named app
RUN adduser -D app
# Add nginx to the app group
RUN adduser nginx app
# Add app to the nginx group
RUN adduser nginx app

# Create the folder for the backend
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN pip3 install --upgrade pip

# Create the static files directory and set permissions
USER root
RUN mkdir -p /var/www/4skl/static/ /var/www/4skl/media/
RUN chown -R app:app /var/www/4skl/
RUN chmod -R 750 /var/www/4skl/

# Create the folder for the backend
WORKDIR /usr/src/app/backend/
COPY skl_backend/ .
RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput
RUN chown -R app:app /usr/src/app/backend/

# Log files
USER root
RUN mkdir -p /var/log/gunicorn/ && touch /var/log/gunicorn/access.log /var/log/gunicorn/access.log  && chown -R app /var/log/gunicorn/
RUN mkdir -p /data/media/
COPY ./media/ /var/www/4skl/


# Starter script
WORKDIR /usr/src/app/
COPY start.sh .
RUN chmod +x start.sh


#* What the container should run when it is started.
USER root

# During development
CMD ["./start.sh"]

# When ready to deploy
# ENTRYPOINT ["/start.sh"]