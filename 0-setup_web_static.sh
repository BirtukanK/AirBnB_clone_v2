#!/usr/bin/env bash
# this script sets web server for deployment of web static

# install nginx if not already installed
if ! command -v nginx &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y nginx
else
        :
fi

# create folder/s if not exist
if [ ! -d "/data" ]; then
        sudo mkdir "/data"
else
        :
fi

if [ ! -d "/data/web_static/" ]; then
        sudo mkdir "/data/web_static/"
else
        :
fi

if [ ! -d "/data/web_static/releases/" ]; then
        sudo mkdir "/data/web_static/releases/"
else
        :
fi

if [ ! -d "/data/web_static/shared/" ]; then
        sudo mkdir "/data/web_static/shared/"
else
        :
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
        sudo mkdir "/data/web_static/releases/test/"
else
        :
fi

if [ ! -e "/data/web_static/releases/test/index.html" ]; then
        sudo touch "/data/web_static/releases/test/index.html"
else
        :
fi
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

if [ -L "/data/web_static/current" ]; then
        sudo rm "/data/web_static/current"
else
        :
fi
ln -s "/data/web_static/releases/test" "/data/web_static/current"

chown -hR ubuntu:ubuntu /data/

sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default


# test syntax erros
sudo nginx -t

# restart config files after change
sudo service nginx restart
