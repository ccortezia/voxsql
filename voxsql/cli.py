import click
from .parser import parse
from .binders import Psycopg2BinderFactory


@click.command(help="""

    Generates application code respective to voxsql frames detected in the given SOURCES,
    where each item in SOURCES is either the path to a readable file or the character -
    that represents the stdin.

    Examples:

        voxsql module.sql

        cat module.sql | voxsql - > generated.py

        cat module_1.sql | voxsql - module_2.sql | tee generate.py

""")
@click.argument('sources', required=True, nargs=-1)
def voxsql_cli(sources):

    source_items = []

    for filename in sources:

        try:
            with click.open_file(filename) as fp:
                source_item = fp.read()

        except OSError as e:
            click.echo(f'Unable to open SOURCE {filename}: [error="{e.strerror}"]', err=True)
            return

        source_items.append(source_item)

    concatenated_sources = '\n'.join(source_items)

    frames = parse(concatenated_sources)

    factory = Psycopg2BinderFactory()

    output_items = [factory.create(frame) for frame in frames]

    contatenated_output = '\n'.join(output_items)

    click.echo(contatenated_output)
