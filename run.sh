#!/bin/bash
tmux new-session "redditScrape"
tmux split-window -d "python redditScrape.py"
tmux split-window -d "python steamScape.py"
tmux split-window -d "python3 discordBot.py"
tmux set -g remain-on-exit on
