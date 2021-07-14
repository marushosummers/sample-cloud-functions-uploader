run:
	docker-compose build
	docker-compose up -d
stop:
	docker-compose down
enter:
	docker-compose exec pythonenv /bin/bash
start:
	docker-compose exec pythonenv pipenv run start
lint:
	docker-compose exec pythonenv pipenv run lint
format:
	docker-compose exec pythonenv pipenv run format
log:
	docker-compose logs -f pythonenv
