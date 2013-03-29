Pay period remaining
=====================

Simple web application which helps to calculate pay periods, remaining in current year.

Current version: pre-alpha

# Server

Run development server:

	python server/app.py

# Client

Build client (into client/public folder):

    cd client && brunch build

Watch client directory and rebuild if something changed:

    cd client && brunch watch

# Nginx configuration example

Assuming that Python-based API is on localhost:8002

    server {
        listen       8001;
        listen       localhost:8001;
        server_name  localhost;

   		location / {
       		root   /path/to/pay-periods-remaining/client/public;
       	}

      location ^~ /api {
          proxy_pass http://localhost:8002;
    	}
	}