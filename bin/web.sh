#!/bin/bash

set -eo pipefail

dirs=('cache' 'logs' 'media' 'sqlite3' 'statiic')
for dir in "${dirs[@]}"; do
  mkdir -p "data/${dir}"
done

./manage.py collectstatic --no-input
./manage.py migrate --no-input

for dir in "${dirs[@]}"; do
  chown -R nobody:nogroup "data/${dir}"
done

gunicorn -w 2 -k gevent -u nobody -g nogroup -b 0.0.0.0:8080 race_condition_playground.wsgi
