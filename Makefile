run_local:
	docker-compose -f local.yml up

deploy:
	python3 scripts/deploy.py
