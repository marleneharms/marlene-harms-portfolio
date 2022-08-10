#!/bin/bash

cd /root/marlene-harms-portfolio
git fetch && git reset origin/main --hard
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build
echo "Everything is working:D"
