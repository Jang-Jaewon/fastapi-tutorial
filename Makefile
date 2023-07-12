build:
	dockst compose build

start:
	docker compose up -d

beauty:
	black . && isort .

db-migrate:
	docker-compose exec app alembic revision --autogenerate -m "${MSG}"

db-upgrade:
	docker-compose exec app alembic upgrade head

app-log:
	docker-compose logs -f app

test:
	docker-compose exec app "pytest"

pip-list:
	docker-compose exec app sh -c "pip list"
