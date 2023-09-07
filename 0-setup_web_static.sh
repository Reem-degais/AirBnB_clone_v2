#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

#Install Nginx
sudo apt-get update
sudo apt-get install -y nginx

#Create the folder /data/,/data/web_static/,/data/web_static/releases/,
#/data/web_static/releases/test/
sudo mkdir -p /data/web_static/releases/test/

#Create the folder /data/web_static/shared/
sudo mkdir -p /data/web_static/shared/

#Create a fake HTML file /data/web_static/releases/test/index.html
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | sudo tee /data/web_static/releases/test/index.html

#Create a symbolic link  If the symbolic link already exists,
#it should be deleted and recreated every time the script is ran
sudo ln -sf /data/web_static/current /data/web_static/releases/test/

#Give ownership of the /data/ folder to the ubuntu user AND group,
#This should be recursive; everything inside should be created/owned
#by this user/group.
sudo chown -hR ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content of
#/data/web_static/current/ to hbnb_static
sudo printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" | sudo tee /etc/nginx/sites-available/default
#restart Nginx
sudo service nginx restart
