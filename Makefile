.PHONY:

.DEFAULT_GOAL := help

test.start.d:
	docker-compose -p voxsql -f tests/e2e/docker-compose.yml up -d

test.stop:
	docker-compose -p voxsql -f tests/e2e/docker-compose.yml stop

test.kill:
	docker-compose -p voxsql -f tests/e2e/docker-compose.yml rm -f

test.setup.pg:
	PGHOST=localhost PGPORT=5432 PGUSER=voxsql PGPASSWORD=voxsql \
	psql -U voxsql -f tests/e2e/pg-setup.sql

test.reset.pg:
	PGHOST=localhost PGPORT=5432 PGUSER=voxsql PGPASSWORD=voxsql \
	psql -U voxsql -f tests/e2e/pg-reset.sql

test.psql:
	PGHOST=localhost PGPORT=5432 PGUSER=voxsql PGPASSWORD=voxsql \
	psql -U voxsql

test.bash.pg:
	docker run -ti --rm -v voxsql_pg-data:/db -w /db ubuntu bash

test.list:
	docker-compose -f tests/e2e/docker-compose.yml -p voxsql ps
