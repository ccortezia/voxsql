
# Design Goals and Inspiration

`voxsql` strives to promote SQL as a first-class language within application-centric projects.

As opposed to ORMs, `voxsql` does not try to encapsulate SQL within higher-level application-level abstractions, nor does it try to rewrite or adapt provided SQL for greater portability. The premise here is that directly writing and maintaing SQL code has some interesting advantages, such as a lower barrier to the usage of more advanced SQL features, easier inspection of queries, and the possibility to reduce application footprint and complexity. It is a fair statement to assume `voxsql` promotes simplicity at the cost of flexibility.

Some of the typically recognized drawbacks of a SQL-heavy design, like the lack of query composability, the difficulty to promote code reuse, and the lack of cross-engine portability are not `voxsql`'s focus, and for that reason, it is considered unsuitable for projects that really need to support an unpredictably complex persistence layer, which might not be as representative of current reality as common sense assumes to be the case these days.

Here are a few projects that promote SQL for application development in slightly different ways:
* [`HugSQL`](https://github.com/layerware/hugsql): DSL-based SQL-bindings generation for Clojure
* [`Yesql`](https://github.com/krisajenkins/yesql/): DSL-based SQL-bindings generation for Clojure
* [`anosql`](https://github.com/honza/anosql): inspired by `Yesql`, for Python.

Listed below are references to material that positively influenced ideas contained in `voxsql`:
* _[Mastering PostgreSQL In Application Development](https://masteringpostgresql.com/), by Dimitri Fontaine_.
