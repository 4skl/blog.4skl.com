#!/bin/sh
# Check nginx configuration
nginx -t

# Reload nginx
nginx -s reload

# Install Certbot and Certbot-nginx
apk add --no-cache certbot certbot-nginx

# Obtain Let's Encrypt certificate
certbot --nginx -d www.4skl.com --non-interactive --agree-tos --email $CERTBOT_EMAIL --redirect

# Stop nginx
nginx -s stop

# Start supervisord
supervisord -c /etc/supervisord.conf