from setuptools import setup, find_packages

setup(
    name='voxsql',
    version='0.1',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        voxsql=voxsql.cli:voxsql_cli
    ''',
)
