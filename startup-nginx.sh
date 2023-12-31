#!/bin/sh

# Check nginx configuration, reload nginx, and obtain Let's Encrypt certificate if none present or renew it if needed, then stop nginx
sh ./certificate-setup.sh

# Start supervisord
supervisord -c /etc/supervisord.conf