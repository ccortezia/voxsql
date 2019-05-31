create schema if not exists voxsql;

create type voxsql.origin as enum ('internal', 'external');

create table voxsql.contacts (
    id serial primary key,
    name varchar(50) unique,
    age int default 10,
    origin origin default 'external',
    constraint sysname check (origin = 'external' or (origin = 'internal' and name = 'system'))
);
