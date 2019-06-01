# voxsql

`voxsql` improves database application development by reading Javadoc-like comments in SQL code.

## Use Cases

Use cases for this library include but are not limited to:
* Automatic generation of human-friendly documentation of SQL excerpts.
* Automatic generation of application-level bindings ([Learn more](docs/code-gen.md)).
* Instrumentation of test code to extend coverage analysis to SQL excerpts.

## Getting Started

`voxsql` works on annotated SQL files. Annotations are provided as Javadoc-like comments, and only properly framed SQL segments are considered by the library when parsing files. Below is an example annotated SQL snippet ready for `voxsql` to process:

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

As opposed to ORMs, `voxsql` does not try to encapsulate SQL within higher-level abstractions and in doing so it gives away some of the flexibility offered by application language constructs. At the same time, a SQL-first approach to persistence design brings some interesting project benefits, such as a lower barrier to the usage of advanced SQL features, easier inspection of queries, and application footprint and complexity reduction. In short, it would be a fair statement to assume `voxsql` brings simplicity at the cost of flexibility.

Some of the typically recognized drawbacks of a SQL-heavy design, like the lack of query composability, the difficulties to promote code reuse, and the lack of cross-engine portability are not `voxsql`'s focus, and for that reason, it is considered unsuitable for projects that really need to support an unpredictably complex persistence layer (which might be fewer cases than recognized by common sense these days).

Here are a few projects that promote SQL for application development in slightly different ways:
* [`HugSQL`](https://github.com/layerware/hugsql): DSL-based SQL-bindings generation for Clojure (active)
* [`Yesql`](https://github.com/krisajenkins/yesql/): DSL-based SQL-bindings generation for Clojure (inactive)
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

* Integrate to CircleCI.
* Integrate to CodeClimate.
* PyPI packaging.
* Automate exception handling by means of a new `@error` tag.
* Add support to `@dialect sqlite`
* Add support to `@dialect mysql`
* Add support to `@dialect xyz:version`
* Add sphinx docs
* Add cli command for lanching the interpreter with bindings preloaded.
