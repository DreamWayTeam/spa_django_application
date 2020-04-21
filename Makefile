run_local:
	docker-compose -f local.yml up

run_production:
	docker-compose -f production.yml up

run_local_rebuild:
	docker-compose -f local.yml up --build

deploy:
	python3 scripts/deploy.py

run_local_shell:
	docker-compose -f local.yml exec django bash
