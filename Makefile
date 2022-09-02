build-p:  # build prod
	docker compose -f "./docker/docker-compose.prod.yml" -p "backend" up --build -d
build-d: # build dev
	docker compose -f "./docker/docker-compose.dev.yml" -p "backend" up --build -d
	uvicorn app:app --reload -- port 443
start:
	docker compose -p "backend" start
stop:
	docker compose -p "backend" stop
up-p: # up production
	docker compose -f "./docker/docker-compose.prod.yml" -p "backend" up -d
up-d: # up development
	docker compose -f "./docker/docker-compose.dev.yml" -p "backend" up -d
	uvicorn app:app --reload --port 443
restart: stop start

clean-data:
	docker system prune -a --volumes

make-migration:
	alembic revision --autogenerate

run-migration:
	alembic upgrade head

#FIXME: Добавить переменные для путей до докер компос

