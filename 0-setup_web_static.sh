#!/usr/bin/env bash
# A script that sets up your web servers for the deployment of web_static
sudo apt update
sudo apt install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo 'Hi, I'\''m Deborah Jimmy, a student of alx' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
CONFIG="server {
        listen 80 default_server;
        listen [::]:80 default_server;
	
	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;      

        server_name _;

	location / {
                # First attempt to serve request as file, then     
                # as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
        }

        location /redirect_me {
		return 301 https://www.alxafrica.com;
        }

        error_page 404 /404.html;
        location /404.html{
                internal;
        }

        location /hbnb_static {
                alias /data/web_static/current/;       
        }
}"

bash -c "echo -e '$CONFIG' > /etc/nginx/sites-available/default"
sudo service nginx restart
