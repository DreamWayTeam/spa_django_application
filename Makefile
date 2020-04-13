run_local:
	docker-compose -f local.yml up

run_local_rebuild:
	docker-compose -f local.yml up --build

deploy:
	python3 scripts/deploy.py
