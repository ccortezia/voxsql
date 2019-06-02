import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

about = {}
exec((HERE / "voxsql/_version.py").read_text(), about)
VERSION = about["__version__"]

setup(
    name='voxsql',
    version=VERSION,
    description='Generate application artifacts from documented SQL code',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/ccortezia/voxsql/',
    author='Cristiano Cortezia',
    author_email='cristiano.cortezia@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        voxsql=voxsql.cli:voxsql_cli
    ''',
)
