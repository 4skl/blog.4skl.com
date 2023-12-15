#!/bin/sh

# Install base initial data
if [ -f "/usr/src/app/backend/fixtures/initial_data.json" ]; then
    su -s /bin/sh -c 'cd backend && \
     source venv/bin/activate && \
     python3 manage.py loaddata fixtures/initial_data.json' app
fi
su -s /bin/sh -c 'cd backend && \
     source venv/bin/activate && \
     gunicorn skl_backend.wsgi:application -b localhost:8000 --access-logfile /var/log/gunicorn/access.log --error-logfile /var/log/gunicorn/error.log &' app

su -s /bin/sh -c 'nginx -g "daemon off;"' nginx