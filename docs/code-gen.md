
# Application Code Generation

Automatic code generation is achieved by transforming parsed frames into application-compliant code. Below is an example of `voxsql` being used to generate a programmatic interface for the SQL excerpt above:

```python
from voxsql import parse
from voxsql.binders import Psycopg2BinderFactory
frames = parse(open('my-module.sql').read())
factory = Psycopg2BinderFactory()
function_code = factory.create(frames[0])
```

The resulting generated code looks like the following:

```python
def add_contact(conn, contact_name=None):
    sql_query = "insert into contacts (name) values (%(contact_name)s) returning name ;"
    sql_params = dict(contact_name=contact_name)
    cursor = conn.cursor()
    cursor.execute(sql_query, sql_params)
    fetched = cursor.fetchall()
    cursor.close()
    return dict(name=fetched[0][0])

assert add_contact("Max the Brawler") == {"name": "Max the Brawler"}
```
