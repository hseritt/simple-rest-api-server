# Simple Rest API Server

This is a very simple Rest API server written using Djago and the Django Rest Framework.

It has a very simple app already included called "events". It can be used with other frontend JS frameworks like Angular or React.

## Set Up

Clone project into a folder.

Install Python 3.8.1 using pyenv (see the Pyenv section on this page for notes on how to install pyenv: https://dev.prodigi.us/post/python-package-and-version-management/).

`$ pyenv install 3.8.1              # Install Python 3.8.1` \
`$ pyenv virtualenv rest-api-server # Set up a virtual environment called rest-api-server` \
`$ pyenv local rest-api-server      # Designates this space as virtual environment container` \
`$ pip install -r requirements.txt  # Installs necessary packages` \

## Run rest-api-server 

`$ python manage.py runserver` \

## View Rest API Response

In a browser go to http://localhost:8000/api/events
