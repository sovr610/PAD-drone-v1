#!/bin/bash

echo "installing node"
sudo apt-get update

curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -

sudo apt-get install -y nodejs

node -v
