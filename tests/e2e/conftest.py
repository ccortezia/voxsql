import os
import pytest
import psycopg2

HERE = os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def pg_schema():
    """Provides the stock database schema SQL"""
    base_path = os.path.normpath(os.path.join(HERE, 'pg-setup.sql'))
    with open(base_path) as f:
        return f.read()


@pytest.fixture(scope='session')
def pg_resetdb():
    """Provides the stock database initialization SQL"""
    initdb_path = os.path.normpath(os.path.join(HERE, 'pg-reset.sql'))
    with open(initdb_path) as f:
        return f.read()


@pytest.fixture(scope='session')
def pg_functions():
    """Provides a voxsql compliant .sql module based on postgresql"""
    base_path = os.path.normpath(os.path.join(HERE, 'pg-functions.sql'))
    with open(base_path) as f:
        return f.read()


@pytest.fixture(scope='session')
def psycopg2_conn():
    """Provides a psycopg2 connection object"""
    return psycopg2.connect(host='localhost', dbname='voxsql', user='voxsql', password='voxsql')


@pytest.fixture(scope='session')
def pg_fresh(psycopg2_conn, pg_schema, pg_resetdb):
    """Ensures the database is reset at the start of each test session execution"""
    cursor = psycopg2_conn.cursor()
    cursor.execute(pg_resetdb)
    cursor.execute(pg_schema)
    psycopg2_conn.commit()
    return psycopg2_conn


@pytest.fixture(scope='function')
def pg_conn(pg_fresh, request):
    """Ensures the database is rolled back at the end of each test function execution"""
    request.addfinalizer(pg_fresh.rollback)
    return pg_fresh
