DJANGO = python manage.py

runserver:
	@$(DJANGO) runserver

makemigrations:
	@$(DJANGO) makemigrations

migrate:
	@$(DJANGO) migrate

test:
	$(DJANGO) test

requirements:
	@pip freeze > requirements.txt

format:
	@black .

build:
	@docker compose -f docker-compose-dev.yaml up --build

enter.container:
	@docker exec -it park_easy_app bash