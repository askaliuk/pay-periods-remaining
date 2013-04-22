Pay periods remaining
=====================

Simple web application which helps to calculate pay periods, remaining in current year.
The main idea behind the project was to create full-stack one page application using Python + JavaScript combination.
It's main purpose is to prepare finished solution for simple real-world problem.
Unfortunately, it lacks lot of UX/UI improvements and features (see TODO).
Deployed on [ppr-askaliuk.rhcloud.com](http://ppr-askaliuk.rhcloud.com/)

# Components, frameworks, tools

  * Backbone
  * Twitter Bootstrap
  * Handlebars templates
  * brunch.io
  * Jquery, LESS/SASS
  * Mocha/Chai for js tests
  * Flask on backend
  * python-dateutil

  Application skeleton: [askalyuk/brunch-fruits](https://github.com/askalyuk/brunch-fruits)

# Dependencies

    cd server && pip install -r requirements.txt
    cd client && npm install

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
    http://ppr-askaliuk.rhcloud.com/static/test/index.html