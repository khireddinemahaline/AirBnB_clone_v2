#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

apt-get -y install update
apt-get -y install nginx
sudo /etc/init.d/nginx start
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "hello world" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/site_available/default
sudo /etc/init.d/nginx restart
exit 0
