#!/bin/sh
# Check nginx configuration
nginx -t

# Reload nginx
nginx -s reload

# Check if certificate exists
if [ ! -d "/etc/letsencrypt/live/www.4skl.com" ]; then
  # Obtain Let's Encrypt certificate
  certbot --nginx -d www.4skl.com --non-interactive --agree-tos --email $CERTBOT_EMAIL --redirect
else
  # Ensure Nginx is configured to use the existing certificate and set up the redirection
  certbot --nginx --keep -d www.4skl.com --non-interactive --agree-tos --email $CERTBOT_EMAIL --redirect
  # Renew Let's Encrypt certificate if due
  certbot renew
  # Ensure Nginx is configured to use the certificate
  certbot install --nginx -d www.4skl.com
fi
# Stop nginx
nginx -s stop