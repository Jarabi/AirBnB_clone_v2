#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

# Install nginx
if ! command nginx -v &>/dev/null;
then
	apt update
	apt install -y nginx
fi

# Create directories (if they don't exist)
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test/

# Create test HTML file
test_dir="/data/web_static/releases/test"
touch "$test_dir"/index.html
echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" | sudo tee "$test_dir"/index.html > /dev/null

# Re/create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/

# Update nginx configuration
old="server_name _;"
new="$old\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web\_static\/current\/;\n\t}"
sed -i "s/$old/$new/" /etc/nginx/sites-available/default
service nginx restart

