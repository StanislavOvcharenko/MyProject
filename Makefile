SHELL := /bin/bash

manage_py := python3 app/manage.py

run:
	$(manage_py) runserver

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate
