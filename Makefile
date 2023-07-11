build:
	docker compose up -d

beauty:
	black . && isort .

db-migrate:
	docker-compose exec web alembic revision --autogenerate -m "${MSG}"

db-upgrade:
	docker-compose exec web alembic upgrade head

web-log:
	docker-compose logs -f web

test:
	docker-compose exec app "pytest"