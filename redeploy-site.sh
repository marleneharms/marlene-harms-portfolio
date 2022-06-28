#!/usr/bin/env bash
tmux kill-server
cd marlene-harms-portfolio
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
systemctl restart myportfolio.service
echo "Everything is working:D"
