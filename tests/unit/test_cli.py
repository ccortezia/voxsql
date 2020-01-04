import os
from click.testing import CliRunner
from voxsql.cli import voxsql_cli


HERE = os.path.abspath(os.path.join(__file__, os.path.pardir))


def test_cli_from_stdin_should_generate_content(sample_data_content):
    runner = CliRunner()
    result = runner.invoke(voxsql_cli, args=['-'], input=sample_data_content)
    print(result.stdout)
    assert len(result.stdout) > 1


def test_cli_from_filename_should_generate_content(sample_data_filepath):
    runner = CliRunner()
    result = runner.invoke(voxsql_cli, args=[sample_data_filepath])
    assert len(result.stdout) > 1


def test_cli_from_filename_with_nonexisting_file_should_err():
    runner = CliRunner(mix_stderr=False)
    result = runner.invoke(voxsql_cli, args=['unknown.sql'])
    assert result.stderr == 'Unable to open SOURCE unknown.sql: [error="No such file or directory"]\n'
