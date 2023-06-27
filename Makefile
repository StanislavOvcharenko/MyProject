SHELL := /bin/bash

manage_py := python3 app/manage.py

run:
	$(manage_py) runserver

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

build_and_run: makemigrations \
	migrate \
	run

shell:
	$(manage_py) shell_plus --print-sql

celery:
	cd app && celery -A settings worker --loglevel=INFO

celerybeat:
	cd app && celery -A settings beat --loglevel=INFO

coverage:
	pytest --cov=app app/tests/ --cov-report html && coverage report --fail-under=95.0000

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"