#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get -y install update
sudo apt-get -y install nginx
sudo /etc/init.d/nginx start
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "hello world" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
exit 0
