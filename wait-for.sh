#!/bin/sh

# The first argument is the service to wait for (in host:port format)
SERVICE=$1
shift

# Extract the host and port from the service
HOST=$(echo $SERVICE | cut -d : -f 1)
PORT=$(echo $SERVICE | cut -d : -f 2)

# Wait for the service to be available
while ! nc -z $HOST $PORT; do
  echo "Waiting for $SERVICE..."
  sleep 1
done