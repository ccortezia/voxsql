from voxsql.binders import Psycopg2BinderFactory
from .utils import codeblock


CASES = (

    # ---------------------------------------------------------------------------------------------

    (
        "GetFieldAsScalar",
        Psycopg2BinderFactory,
        codeblock(
            """
            /**
             *
             * Performs a database operation.
             *
             * @dialect postgresql
             * @name get_first_contact_name
             * @retmode scalar
             */
            {
                select name
                from contacts
                limit 1
                ;
            }
            """
        ),
        codeblock(
            """
            def get_first_contact_name(conn):
                sql_query = "select name from contacts limit 1 ;"
                sql_params = dict()
                cursor = conn.cursor()
                cursor.execute(sql_query, sql_params)
                fetched = cursor.fetchall()
                cursor.close()
                return fetched[0][0]
            """
        ),
    ),

    # ---------------------------------------------------------------------------------------------

    (
        "GetEntryAsTuple",
        Psycopg2BinderFactory,
        codeblock(
            """
            /**
             *
             * Performs a database operation.
             *
             * @dialect postgresql
             * @name get_first_contact
             * @retmode tuple
             */
            {
                select *
                from contacts
                limit 1
                ;
            }
            """
        ),
        codeblock(
            """
            def get_first_contact(conn):
                sql_query = "select * from contacts limit 1 ;"
                sql_params = dict()
                cursor = conn.cursor()
                cursor.execute(sql_query, sql_params)
                fetched = cursor.fetchall()
                cursor.close()
                return fetched[0]
            """
        ),
    ),

    # ---------------------------------------------------------------------------------------------

    (
        "GetEntriesAsTuples",
        Psycopg2BinderFactory,
        codeblock(
            """
            /**
             *
             * Performs a database operation.
             *
             * @dialect postgresql
             * @name get_contacts
             * @retmode tuples
             */
            {
                select *
                from contacts
                ;
            }
            """
        ),
        codeblock(
            """
            def get_contacts(conn):
                sql_query = "select * from contacts ;"
                sql_params = dict()
                cursor = conn.cursor()
                cursor.execute(sql_query, sql_params)
                fetched = cursor.fetchall()
                cursor.close()
                return fetched
            """
        ),
    ),

    # ---------------------------------------------------------------------------------------------

    (
        "GetEntryAsRecordNoField",
        Psycopg2BinderFactory,
        codeblock(
            """
            /**
             *
             * Performs a database operation.
             *
             * @dialect postgresql
             * @name get_first_contact
             * @retmode record
             */
            {
                select *
                from contacts
                limit 1
                ;
            }
            """
        ),
        codeblock(
            """
            def get_first_contact(conn):
                sql_query = "select * from contacts limit 1 ;"
                sql_params = dict()
                cursor = conn.cursor()
                cursor.execute(sql_query, sql_params)
                fetched = cursor.fetchall()
                cursor.close()
                return dict()
            """
        ),
    ),

    # ---------------------------------------------------------------------------------------------

    (
        "GetEntryAsRecordOneField",
        Psycopg2BinderFactory,
        codeblock(
            """
            /**
             *
             * Performs a database operation.
             *
             * @dialect postgresql
             * @name get_first_contact
             * @retmode record
             * @retval name: string
             */
            {
                select *
                from contacts
                limit 1
                ;
            }
            """
        ),
        codeblock(
            """
            def get_first_contact(conn):
                sql_query = "select * from contacts limit 1 ;"
                sql_params = dict()
                cursor = conn.cursor()
                cursor.execute(sql_query, sql_params)
                fetched = cursor.fetchall()
                cursor.close()
                return dict(name=fetched[0][0])
            """
        ),
    ),

    # ---------------------------------------------------------------------------------------------

    (
        "GetEntryAsRecordMultipleFields",
        Psycopg2BinderFactory,
        codeblock(
            """
            /**
             *
             * Performs a database operation.
             *
             * @dialect postgresql
             * @name get_first_contact
             * @retmode record
             * @retval age: number
             * @retval name: string
             */
            {
                select *
                from contacts
                limit 1
                ;
            }
            """
        ),
        codeblock(
            """
            def get_first_contact(conn):
                sql_query = "select * from contacts limit 1 ;"
                sql_params = dict()
                cursor = conn.cursor()
                cursor.execute(sql_query, sql_params)
                fetched = cursor.fetchall()
                cursor.close()
                return dict(age=fetched[0][0], name=fetched[0][1])
            """
        ),
    ),

    # ---------------------------------------------------------------------------------------------

    (
        "GetEntriesAsRecordsNoField",
        Psycopg2BinderFactory,
        codeblock(
            """
            /**
             *
             * Performs a database operation.
             *
             * @dialect postgresql
             * @name get_contacts
             * @retmode records
             */
            {
                select *
                from contacts
                limit 1
                ;
            }
            """
        ),
        codeblock(
            """
            def get_contacts(conn):
                sql_query = "select * from contacts limit 1 ;"
                sql_params = dict()
                cursor = conn.cursor()
                cursor.execute(sql_query, sql_params)
                fetched = cursor.fetchall()
                cursor.close()
                return [dict() for row in fetched]
            """
        ),
    ),

    # ---------------------------------------------------------------------------------------------

    (
        "GetEntriesAsRecordsSingleField",
        Psycopg2BinderFactory,
        codeblock(
            """
            /**
             *
             * Performs a database operation.
             *
             * @dialect postgresql
             * @name get_contacts
             * @retmode records
             * @retval name: string
             */
            {
                select *
                from contacts
                limit 1
                ;
            }
            """
        ),
        codeblock(
            """
            def get_contacts(conn):
                sql_query = "select * from contacts limit 1 ;"
                sql_params = dict()
                cursor = conn.cursor()
                cursor.execute(sql_query, sql_params)
                fetched = cursor.fetchall()
                cursor.close()
                return [dict(name=row[0]) for row in fetched]
            """
        ),
    ),

    # ---------------------------------------------------------------------------------------------

    (
        "GetEntriesAsRecordsMultipleFields",
        Psycopg2BinderFactory,
        codeblock(
            """
            /**
             *
             * Performs a database operation.
             *
             * @dialect postgresql
             * @name get_contacts
             * @retmode records
             * @retval age: number
             * @retval name: string
             */
            {
                select *
                from contacts
                limit 1
                ;
            }
            """
        ),
        codeblock(
            """
            def get_contacts(conn):
                sql_query = "select * from contacts limit 1 ;"
                sql_params = dict()
                cursor = conn.cursor()
                cursor.execute(sql_query, sql_params)
                fetched = cursor.fetchall()
                cursor.close()
                return [dict(age=row[0], name=row[1]) for row in fetched]
            """
        ),
    ),

    # ---------------------------------------------------------------------------------------------

    (
        "InsertEntrySingleParameterReturnRecord",
        Psycopg2BinderFactory,
        codeblock(
            """
            /**
             *
             * Performs a database operation.
             *
             * @dialect postgresql
             * @name add_contact
             * @param contact_name: string - the target contact's name
             * @retmode record
             * @retval name: string
             * @retval age: number
             * @retval created_at: datetime
             */
            {
                insert into contacts (name)
                values (%(contact_name)s)
                returning name, age, created_at
                ;
            }
            """
        ),
        codeblock(
            """
            def add_contact(conn, contact_name=None):
                sql_query = "insert into contacts (name) values (%(contact_name)s) returning name, age, created_at ;"
                sql_params = dict(contact_name=contact_name)
                cursor = conn.cursor()
                cursor.execute(sql_query, sql_params)
                fetched = cursor.fetchall()
                cursor.close()
                return dict(name=fetched[0][0], age=fetched[0][1], created_at=fetched[0][2])
            """
        ),
    ),

    # ---------------------------------------------------------------------------------------------

    (
        "InsertEntryMultipleParametersReturnRecord",
        Psycopg2BinderFactory,
        codeblock(
            """
            /**
             *
             * Performs a database operation.
             *
             * @dialect postgresql
             * @name add_contact
             * @param contact_name: string - the target contact's name
             * @param age: number - the target contact's age
             * @retmode record
             * @retval name: string
             */
            {
                insert into contacts (name, age)
                values (%(contact_name)s, %(age)s)
                returning name, age, created_at
                ;
            }
            """
        ),
        codeblock(
            """
            def add_contact(conn, contact_name=None, age=None):
                sql_query = "insert into contacts (name, age) values (%(contact_name)s, %(age)s) returning name, age, created_at ;"
                sql_params = dict(contact_name=contact_name, age=age)
                cursor = conn.cursor()
                cursor.execute(sql_query, sql_params)
                fetched = cursor.fetchall()
                cursor.close()
                return dict(name=fetched[0][0])
            """
        ),
    ),

)
