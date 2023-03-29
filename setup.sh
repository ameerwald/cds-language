#!/usr/bin/env bash

# install hdbscan for BERTopic
sudo apt-get update
sudo apt-get install python3-dev

# requirements
pip install --upgrade pip
pip install --upgrade nbformat
python3 -m pip install -r requirements.txt
>>>>>>> 52da4eb463d16bfca02f995c5dad9056e2bfb02c
