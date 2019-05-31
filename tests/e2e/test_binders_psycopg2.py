from voxsql.binders import Psycopg2BinderFactory
from .utils import load_functions


def test_psycopg2_bind_exec(pg_conn, pg_functions):

    functions = load_functions(pg_functions, Psycopg2BinderFactory)
    add_contact = functions['add_contact']
    add_contact_details = functions['add_contact_details']
    list_contacts_as_records = functions['list_contacts_as_records']
    list_contacts_as_tuples = functions['list_contacts_as_tuples']
    get_contact_age_by_name = functions['get_contact_age_by_name']

    returned = add_contact(pg_conn, "Joe the Brave")
    assert returned == {"name": "Joe the Brave"}

    add_contact_details(pg_conn, "Ann the Thunder", 23)

    returned = list_contacts_as_records(pg_conn)
    assert returned == [
        {"name": "Joe the Brave", "age": 10},
        {"name": "Ann the Thunder", "age": 23}
    ]

    returned = list_contacts_as_tuples(pg_conn)
    assert returned == [
        ("Joe the Brave", 10),
        ("Ann the Thunder", 23),
    ]

    returned = get_contact_age_by_name(pg_conn, "Joe the Brave")
    assert returned == 10

    returned = get_contact_age_by_name(pg_conn, "Ann the Thunder")
    assert returned == 23
