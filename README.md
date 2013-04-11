Pay period remaining
=====================

Simple web application which helps to calculate pay periods, remaining in current year.

Current version: alpha

# Server

Run development server:

	python server/app.py

Run server tests:

  server/run_tests.sh

# Client

Build development client (into client/public folder):

    cd client && brunch build

Watch client directory and rebuild if something changed:

    cd client && brunch watch

Production build:

    cd client && brunch build --optimize

Client tests (on browser):

    http://localhost:8002/static/test/index.html