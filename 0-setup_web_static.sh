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
sudo sed -i '53i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

#restart Nginx
sudo service nginx restart
