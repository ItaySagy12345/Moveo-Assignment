init:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt

destroy:
	rm -rf venv

build:
	docker compose up --build

up:
	docker compose up

down:
	docker compose down
	docker rmi server
	docker image prune
	docker volume prune