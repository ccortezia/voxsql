[![PyPI version](https://badge.fury.io/py/voxsql.svg)](https://badge.fury.io/py/voxsql) [![CircleCI](https://circleci.com/gh/ccortezia/voxsql/tree/master.svg?style=svg)](https://circleci.com/gh/ccortezia/voxsql/tree/master) [![Maintainability](https://api.codeclimate.com/v1/badges/e923a96d98200af83af6/maintainability)](https://codeclimate.com/github/ccortezia/voxsql/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/e923a96d98200af83af6/test_coverage)](https://codeclimate.com/github/ccortezia/voxsql/test_coverage)

# voxsql

Generates application artifacts from documented SQL code.


## Use Cases

Use cases for this library include but are not limited to:
* Automatic generation of human-friendly documentation of SQL excerpts.
* Automatic generation of application-level bindings ([Learn more](docs/code-gen.md)).
* Instrumentation of test code to extend coverage analysis to SQL excerpts.

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
voxsql sample.sql
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

## Design Goals and Inspiration

`voxsql` strives to promote SQL as a first-class language within application-centric projects.

As opposed to ORMs, `voxsql` does not try to encapsulate SQL within higher-level application-level abstractions, nor does it try to rewrite or adapt provided SQL for greater portability. The premise here is that directly writing and maintaing SQL code has some interesting advantages, such as a lower barrier to the usage of more advanced SQL features, easier inspection of queries, and the possibility to reduce application footprint and complexity. It is a fair statement to assume `voxsql` promotes simplicity at the cost of flexibility.

Some of the typically recognized drawbacks of a SQL-heavy design, like the lack of query composability, the difficulty to promote code reuse, and the lack of cross-engine portability are not `voxsql`'s focus, and for that reason, it is considered unsuitable for projects that really need to support an unpredictably complex persistence layer, which might not be as representative of current reality as common sense assumes to be the case these days.

Here are a few projects that promote SQL for application development in slightly different ways:
* [`HugSQL`](https://github.com/layerware/hugsql): DSL-based SQL-bindings generation for Clojure
* [`Yesql`](https://github.com/krisajenkins/yesql/): DSL-based SQL-bindings generation for Clojure
* [`anosql`](https://github.com/honza/anosql): inspired by `Yesql`, for Python.

Listed below are references to material that positively influenced ideas contained in `voxsql`:
* _[Mastering PostgreSQL In Application Development](https://masteringpostgresql.com/), by Dimitri Fontaine_.

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
