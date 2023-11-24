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


# Backend setup
# Create the folder for the backend
WORKDIR /usr/src/app/backend/
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN pip3 install --upgrade pip
RUN adduser -D app
COPY skl_backend/ .
RUN chown -R app .
RUN pip3 install -r requirements.txt
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate
RUN mkdir -p /var/log/gunicorn/ && touch /var/log/gunicorn/access.log /var/log/gunicorn/access.log && chown -R app /var/log/gunicorn/


# Reverse proxy setup
RUN apk add --no-cache nginx
RUN mkdir -p /var/log/nginx/
RUN chown -R nginx:nginx /var/www/4skl /var/lib/nginx/ /var/log/nginx/
WORKDIR /etc/nginx/http.d/
COPY default.conf default.conf


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