[![PyPI version](https://badge.fury.io/py/voxsql.svg)](https://badge.fury.io/py/voxsql) [![CircleCI](https://circleci.com/gh/ccortezia/voxsql/tree/master.svg?style=svg)](https://circleci.com/gh/ccortezia/voxsql/tree/master) [![Maintainability](https://api.codeclimate.com/v1/badges/e923a96d98200af83af6/maintainability)](https://codeclimate.com/github/ccortezia/voxsql/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/e923a96d98200af83af6/test_coverage)](https://codeclimate.com/github/ccortezia/voxsql/test_coverage)

# voxsql

Generates application artifacts from documented SQL code.


## Use Cases

Use cases for this library include but are not limited to:
* Automatic generation of human-friendly documentation of SQL excerpts.
* Automatic generation of application-level bindings ([Learn more](docs/code-gen.md)).
* Instrumentation of test code to extend coverage analysis to SQL excerpts.

For more information about the design, refer to the [design notes](docs/design.md).

## Getting Started

```
pip install voxsql
```

## Basic Concepts

`voxsql` works on annotated SQL files. Annotations are provided as Javadoc-like comments, and only properly framed SQL segments are considered by the library when parsing files. Below is an example:

```sql
/**
 * Adds a contact to the database.
 *
 * @dialect postgresql
 * @name add_contact
 * @param contact_name: string - the target contact's name
 * @retmode record
 * @retval name: string
 */
{
    insert into contacts (name)
    values (%(contact_name)s)
    returning name
    ;
}
```

_Save the snippet above to `sample.sql` to run the examples below._

## CLI Usage

To digest the SQL file above using the CLI:

```shell
cat queries.sql | voxsql -  # JSON output
cat queries.sql | voxsql - --template=python-psycopg2.j2  # Python output from SQL (implicit JSON conversion step)
cat queries.sql | voxsql - | voxsql --template=python-psycopg2.j2  # Python output from JSON
```

For more information run `voxsql --help`.

## Direct Library Usage

Below is an example on how you can manipulate the file above using the Python library directly:

```python
from voxsql import parse
frames = parse(open('sample.sql').read())
assert frames[0].header.name == 'add_contact'
assert frames[0].body.source.startswith('insert into contacts')
```

## Contributing

This is how you run tests locally:

```shell
make test.start.d
pytest
```

## Roadmap

* Automate exception handling by means of a new `@error` tag.
* Raise spec mismatch during execution
* Add support to `@retmode columns`
* Add support to `@retmode column`
* Add support to mandatory/optional parameter annotation
* Solve design question about passing default column values as parameters
* Solve design question about skipping reseting columns to avoid select-before-update issue
* Add support to `@dialect sqlite`
* Add support to `@dialect mysql`
* Add support to `@dialect xyz:version`
* Add sphinx docs
* Add cli command for lanching the interpreter with bindings preloaded.
