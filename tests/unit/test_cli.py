import os
from click.testing import CliRunner
from voxsql.cli import voxsql_cli
from .utils import codeblock


HERE = os.path.abspath(os.path.join(__file__, os.path.pardir))


EXPECTED = codeblock("""
    def add_contact(conn, contact_name=None):
        sql_query = "insert into contacts (name) values (%(contact_name)s) returning id, name ;"
        sql_params = dict(contact_name=contact_name)
        cursor = conn.cursor()
        cursor.execute(sql_query, sql_params)
        fetched = cursor.fetchall()
        cursor.close()
        return dict(contact_id=fetched[0][0], contact_name=fetched[0][1])

""")


def test_cli_from_stdin_should_generate_expected_content(sample_data_content):
    runner = CliRunner()
    result = runner.invoke(voxsql_cli, args=['-'], input=sample_data_content)
    assert EXPECTED == result.stdout


def test_cli_from_filename_should_generate_expected_content(sample_data_filepath):
    runner = CliRunner()
    result = runner.invoke(voxsql_cli, args=[sample_data_filepath])
    assert EXPECTED == result.stdout


def test_cli_from_filename_with_nonexisting_file_should_err():
    runner = CliRunner(mix_stderr=False)
    result = runner.invoke(voxsql_cli, args=['unknown.sql'])
    assert result.stderr == 'Unable to open SOURCE unknown.sql: [error="No such file or directory"]\n'
