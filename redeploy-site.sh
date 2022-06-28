#!/usr/bin/env bash
tmux kill-server
cd marlene-harms-portfolio
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s ENTER
tmux detach -s ENTER
tmux send-keys -t 0 "flask run --host="0.0.0.0"" ENTER
systemctl restart myportfolio.service
echo "Everything is working:D"
