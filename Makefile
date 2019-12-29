.PHONY:

.DEFAULT_GOAL := help

test.infra.start:
	docker-compose -p voxsql -f tests/e2e/docker-compose.yml up -d

test.infra.stop:
	docker-compose -p voxsql -f tests/e2e/docker-compose.yml stop

test.infra.kill:
	docker-compose -p voxsql -f tests/e2e/docker-compose.yml rm -f

test.infra.list:
	docker-compose -f tests/e2e/docker-compose.yml -p voxsql ps

test.infra.setup:
	PGHOST=localhost PGPORT=5432 PGUSER=voxsql PGPASSWORD=voxsql \
	psql -U voxsql -f tests/e2e/pg-setup.sql

test.infra.reset:
	PGHOST=localhost PGPORT=5432 PGUSER=voxsql PGPASSWORD=voxsql \
	psql -U voxsql -f tests/e2e/pg-reset.sql

test.infra.psql:
	PGHOST=localhost PGPORT=5432 PGUSER=voxsql PGPASSWORD=voxsql \
	psql -U voxsql

test.infra.shell:
	docker run -ti --rm -v voxsql_pg-data:/db -w /db ubuntu bash


build: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist build voxsql.egg-info
	find . -name "*.pyc" -delete
	rm -f .coverage coverage.xml
	rm -rf htmlcov .pytest_cache __pycache__

publish:
	twine upload dist/*

publish.fake:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
